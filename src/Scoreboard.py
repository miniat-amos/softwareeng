import os
import SETTINGS
import string
import re
from datetime import datetime
from sortedcontainers import SortedList
import pygame
from pygame import Surface
from pygame import Rect
from Renderable import Renderable

# .sb - Scoreboard file
# .sba - Scoreboard archive file (contains any scores that couldn't load properly)

# Format of scoreboard files
#	[Score] [Username] [Datetime: %Y/%m/%d-%H:%M:%S]

# Move to settings:
SB_DIR = "Scores/"
SB_FILE = "Scores.sb"
ARCHIVE_DIR = SB_DIR + "Archive/"


DT_FORMAT = "%Y/%m/%d-%H:%M:%S"

USR_CHAR_COUNT = 3
SCORE_DIGIT_COUNT = 12
NAME_FORM = re.compile("^[A-Z]{%d}$" % USR_CHAR_COUNT)

SCORE_HEADER = "Score"
USER_HEADER = "Username"
DATE_HEADER = "Date"

SCROLL_AMOUNT = 12

def tobounds(n, mini, maxi): return max(mini, min(maxi, n))


class Score():

	def __init__(self, line:str = "") -> None:
		self.score = False
		self.username = False
		self.date = False
		if line == "": return

		str_list:list[str] = line.split(' ')
		if len(str_list) < 3:
			print("Too few elements in generic text score line (%d)" % len(str_list))
			return
		
		self.setScore(str_list[0])
		self.setUsername(str_list[1])
		self.setDate(str_list[2])
	

	@property
	def valid(self): return \
		isinstance(self.score,int) \
		and self.username \
		and self.date


	def setScore(self, score) -> bool:
		if isinstance(score, int):
			if score >= 0:
				self.score = score
				return True
			else:
				print("Negative scores are invalid")
				self.score = False
				return False
		elif isinstance(score, str):
			try:
				self.score:int = int(score)
				return True
			except:
				self.score = False
				return False
		else:
			self.score = False
			return False
	
	def setUsername(self, user:str) -> bool:
		try:
			username = NAME_FORM.match(user)
			self.username:str = username.string
			return True
		except:
			username = False
			return False
	
	def setDate(self, date) -> bool:
		if isinstance(date, str):
			try:
				self.date:datetime = datetime.strptime(date, DT_FORMAT)
				return True
			except:
				self.date = False
				return False
		elif isinstance(date, datetime):
			self.date = date
			return True
		else:
			self.date = False
			return False


	def scoreStr(self): return str(self.score)
	def userStr(self): return self.username
	def dateStr(self): return self.date.strftime(DT_FORMAT)
	
	def __str__(self) -> str:
		return	self.score.__str__() + \
				" " + self.username + \
				" " + self.date.strftime(DT_FORMAT)
		pass

	
	def fullDetailStr(self) -> str:
		return "Score: " + self.score.__str__() + \
				" | Username: " + self.username + \
				" | Date: " + self.date.strftime(DT_FORMAT)
		pass

# Functions used is sorting lists of scores
def sortScore(obj:Score): return (-obj.score, obj.date, obj.username)
def sortDate(obj:Score): return (obj.date, -obj.score, obj.username)
def sortUser(obj:Score): return (obj.username, -obj.score, obj.date)

# If the desired filepath given already exists, modify until it's unique, return the first unique one
def getNewFilePath(desired_fp:str):
	while os.path.exists(desired_fp):
		dp = desired_fp.rfind('.')
		desired_fp = desired_fp[:dp] + '.' + desired_fp[dp:]
	return desired_fp


class UsernameTextBox(Renderable):
	def __init__(self, font:pygame.font.Font = -1, v_padding = 8, h_padding = 12):
		super().__init__()
		self.v_padding = v_padding
		self.h_padding = h_padding
		self.typing = False
		self.need_redraw_text = True
		self.text = "___"

		self.font = font

	def update(self):
		if self.need_redraw_text:
			self.redrawText()
		
		self.need_redraw_text = False

	# Takes in the cursor position of a click and checks if the box was clicked
	def checkClick(self, click_pos:tuple[int,int]):
		if self.get_rect().collidepoint(click_pos):
			self.typing = True
		else:
			self.typing = False


	@property
	def font(self): return self.__font
	@font.setter
	def font(self, set:pygame.font.Font):
		if set != -1:
			self.__font:pygame.font.Font = set
		else:
			self.__font:pygame.font.Font = pygame.font.Font(None, 24)
		self.calcDimensions()

	# Takes in a string of key inputs and tries to type them
	def keyInput(self, input:str):
		for char in input:
			try:
				i = self.text.index('_')
				if char.isalpha():
					self.text = self.text[:i] + char.upper() + self.text[i+1:]
			except:
				return # No "empty" spaces (underscores)
		self.need_redraw_text = True

	def backspace(self):
		try:
			i = self.text.index('_')
			if i > 0:
				self.text = self.text[:i-1] + '_' + self.text[i:]
			else:
				return
		except:
			self.text = self.text[:2] + '_'
		self.need_redraw_text = True

	# Redraw the text box
	def redrawText(self):
		self.surface.fill((0,0,0))
		Scoreboard.drawBorders(self.surface)
		self.surface.blit(self.font.render(self.text, True, SETTINGS.HD_TEXT_COLOR), (self.h_padding, self.v_padding))
		pass
	
	# Recalculate dimensions of the text box (size is automatically set based on font)
	def calcDimensions(self):
		text_size = self.font.size('OOO')
		self.size = (
			text_size[0] + self.h_padding * 2,
			text_size[1] + self.v_padding * 2
		)
		self.surface = Surface(self.size, pygame.SRCALPHA)

	# Returns True when user has entered a valid username (meaning text box no longet need)
	def addScore(self, score_n:int, date:datetime) -> bool:
		score_sb = Score()
		if not score_sb.setUsername(self.text):
			print("Username must be exactly 3 alphabetical characters")
			return False
		
		if not score_sb.setScore(score_n):
			print("Internal error: Invalid score (", score_n, ")")
		if not score_sb.setDate(date):
			print("Internal error: Invalid datetime (", date, ")")

		Scoreboard.insertScore(score_sb)



# Scoreboard class
#	Static Elements
#		- Score lists: scores_by_scores, scores_by_date, scores_by_user
#		- loadScores(), inserScore(), exportScores(), __loadFile(), __archiveScores()
#	Non-Static Elements:
#		- Surface
#			- Area of scoreboard display
#			- Acts as a window, through which you can view part or all of the Contents and Header
#		- Contents
#			- An internal scoreboard that can exceed the size of the viewable area

class Scoreboard(Renderable):

	def __init__(self, size:tuple[int,int], font = -1, row_padding = 8, col_padding = 12) -> None:
		super().__init__()
		if not Scoreboard.scores_loaded: Scoreboard.loadScores()

		self.contents:Surface = 0
		self.header:Surface = 0
		
		self.col_padding = col_padding
		self.row_padding = row_padding
		self.index = 0
		self.scroll_pos = [0,0]

		self.need_redraw_window = True
		self.need_redraw_contents = True
		self.need_full_redraw = True
		self.old_scroll = [-1,-1]
		self.old_index = -1

		self.active_score_list = Scoreboard.scores_by_score
		self.reverse_order = False
		
		self.size = size
		self.font = font
	
	
	def update(self):
		### SCROLL ADJUSTMENTS ###

		# Prevent from scrolling below scoreboard
		dist_from_bottom = (Scoreboard.getCnt() - self.index + 1) * self.row_height - (self.u_height-1) - self.scroll_pos[1]
		if dist_from_bottom < 0:
				self.scroll_pos[1] += dist_from_bottom
		
		# If scrolled below existing contents pane
		if self.contents.get_height() - self.scroll_pos[1] - self.height < 0:
			d_index = self.scroll_pos[1] // self.row_height
			self.index += d_index
	
			if self.index > Scoreboard.getCnt():
				self.index = Scoreboard.getCnt() - 1
				self.scroll_pos[1] = 0
			else:
				self.scroll_pos[1] -= d_index * self.row_height
		
		# If scrolling above existing contents pane
		elif self.scroll_pos[1] < 0:
			if self.index <= 0:
				self.scroll_pos[1] = 0
				self.index = 0
			else:
				legnth_off_bottom = self.contents.get_height() - self.scroll_pos[1] - self.height
				d_index = -legnth_off_bottom // self.row_height
				self.index += d_index

				if self.index < 0:
					self.index = 0
					self.scroll_pos[1] = 0
				else:
					self.scroll_pos[1] -= d_index * self.row_height

		# Bound x-scroll to the x-bounds of the contents pane
		self.scroll_pos[0] = tobounds(self.scroll_pos[0], 0, self.contents.get_width() - self.width + 2)


		### REDRAWING ###

		if self.need_full_redraw:
			self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
			self.redrawHeader()
			self.need_redraw_window = True
			self.need_redraw_contents = True
		
		# If scroll has changed, redraw window
		if self.scroll_pos[0] != self.old_scroll[0] \
			or self.scroll_pos[1] != self.old_scroll[1] \
			or self.index == self.old_index:
			
			self.need_redraw_contents = True
			self.need_redraw_window = True
		
		if self.need_redraw_contents:
			self.redrawContents()
			self.need_redraw_window = True

		if self.need_redraw_window:
			self.redrawWindow()
		
		# Reset update check conditions
		self.need_redraw_window = False
		self.need_redraw_contents = False
		self.need_full_redraw = False
		self.old_scroll = self.scroll_pos.copy()
		self.old_index = self.index


	def checkClick(self, global_pos:tuple[int,int]):
		if not self.get_rect().collidepoint(global_pos): return
		
		# Get position of click relative to the scoreboard
		x = global_pos[0] - self.left
		y = global_pos[1] - self.top
		
		# Check if header has been clicked
		if (1 < y <= self.row_height) and (1 <= x <= self.width-1):
			self.need_redraw_window = True
			self.index = 0
			self.scroll_pos = [0,0]

			# Change sort order
			if x < self.div1_x: # Clicked on score
				if self.active_score_list == Scoreboard.scores_by_score:
					self.reverse_order = not self.reverse_order
				else:
					self.active_score_list = Scoreboard.scores_by_score
			elif x < self.div2_x: # Clicked on username
				if self.active_score_list == Scoreboard.scores_by_user:
					self.reverse_order = not self.reverse_order
				else:
					self.active_score_list = Scoreboard.scores_by_user
			else:
				if self.active_score_list == Scoreboard.scores_by_date:
					self.reverse_order = not self.reverse_order
				else:
					self.active_score_list = Scoreboard.scores_by_date


	# Scrolls the contents pane. Validation of scroll is checked in update()
	def scroll(self, mouse_pos:tuple[int,int], down:bool):
		if not self.get_rect().collidepoint(mouse_pos): return

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
			axis = 0
		else:
			axis = 1
		
		if down:
			self.scroll_pos[axis] += SCROLL_AMOUNT
		else:
			self.scroll_pos[axis] -= SCROLL_AMOUNT

	def scrollUp(self, mouse_pos:tuple[int,int]): self.scroll(mouse_pos, False)
	def scrollDown(self, mouse_pos:tuple[int,int]): self.scroll(mouse_pos, True)


	# Two opposing corners of the area of the rect
	@property
	def span(self): return (self.topleft, self.topright)
	@span.setter
	def span(self, set:tuple[tuple[int,int], tuple[int,int]]):
		top = min(set[0][1], set[1][1])
		left = min(set[0][0], set[1][0])
		width = abs(set[0][0] - set[1][0])
		height = abs(set[0][1] - set[1][1])
		self.set_rect(Rect(top, left, width, height))
		self.calcDimensions()

	@property
	def font(self): return self.__font
	@font.setter
	def font(self, set:pygame.font.Font):
		if set != -1:
			self.__font:pygame.font.Font = set
		else:
			self.__font:pygame.font.Font = pygame.font.Font(None, 24)
		self.calcDimensions()


	# Recalculates various aspects such as R/L padding, row height, width of each column, etc.
	def calcDimensions(self):
		char_size = self.font.size('_')
		self.line_height = char_size[1]

		self.u_height = self.height-2
		self.u_width = self.width-2

		self.score_w = max(
			self.font.size('0'*SCORE_DIGIT_COUNT)[0], # char_x*SCORE_DIGIT_COUNT, 
			self.font.size(SCORE_HEADER)[0] # char_x*len(SCORE_HEADER)
		)
		self.user_w = max(
			self.font.size('_'*USR_CHAR_COUNT)[0], # char_x*USR_CHAR_COUNT, 
			self.font.size(USER_HEADER)[0] # char_x*len(USER_HEADER)
		)
		self.date_w = max(
			self.font.size(DT_FORMAT)[0], # char_x*len(DT_FORMAT), 
			self.font.size(DATE_HEADER)[0] # char_x*len(DATE_HEADER)
		)
		
		tot_content_width = self.score_w + self.user_w + self.date_w + 6*self.col_padding
		extra_col_space = self.u_width - tot_content_width
		
		# If scores go off of scoreboard on right
		if extra_col_space < 0:
			con_width = tot_content_width
			head_width = tot_content_width

			self.left_padding = self.col_padding
			self.right_padding = self.col_padding
		# If scores fit on scoreboard
		else:
			con_width = self.u_width
			head_width = self.u_width

			self.left_padding = self.col_padding
			self.right_padding = self.col_padding + extra_col_space // 3
		
		# Get sizes of contents and header
		content_rows = self.u_height // self.line_height + 5
		con_height = content_rows * self.line_height
		self.row_height = self.line_height + 2*self.row_padding
		# Define surfaces for contents and header
		self.contents = Surface((con_width, con_height), pygame.SRCALPHA)
		self.header = Surface((head_width, self.row_height), pygame.SRCALPHA)
		
		# Define x positions of column contents and dividers
		self.score_x = self.left_padding
		self.div1_x = self.score_x + self.score_w + self.right_padding
		self.user_x = self.div1_x + self.left_padding
		self.div2_x = self.user_x + self.user_w + self.right_padding
		self.date_x = self.div2_x + self.left_padding
		
		self.need_full_redraw = True

	# Draws borders around the given surface in the given color
	def drawBorders(surf:Surface, col:tuple[int,int,int,int] = (255,255,255,255)):
		rect = surf.get_rect()
		right, bottom = rect.right-1, rect.bottom-1
		left, top = rect.left, rect.top
		pygame.draw.line(surf, col, (left, top), (right, top))
		pygame.draw.line(surf, col, (left, bottom), (right, bottom))
		pygame.draw.line(surf, col, (left, top), (left, bottom))
		pygame.draw.line(surf, col, (right, top), (right, bottom))
	# Draws column dividers given the x-values of each divider and a color
	def drawColDivides(surf:Surface, lines:list[int], col:tuple[int,int,int,int] = (255,255,255,255)):
		rect = surf.get_rect()
		top, bottom = rect.top, rect.bottom-1
		for line_x in lines:
			pygame.draw.line(surf, col, (line_x, top), (line_x, bottom))

	# Redraws everything from scratch
	def redraw(self):
		self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
		self.redrawHeader()
		self.redrawContents()
		self.redrawWindow()

	# Redraws the the visible portion of contents and header
	def redrawWindow(self):
		self.surface.fill(SETTINGS.SB_BACKGROUND_COLOR)

		head_area = Rect(
			self.scroll_pos[0],
			0,
			self.width,
			self.row_height
		)
		self.surface.blit(self.header, (1,1), head_area)

		cont_area = Rect(
			self.scroll_pos[0],
			self.scroll_pos[1],
			self.width,
			self.height - self.row_height
		)
		self.surface.blit(self.contents, (1,self.row_height+1), cont_area)

		Scoreboard.drawBorders(self.surface)

	# Redraws the entire header
	def redrawHeader(self):
		self.header.fill(SETTINGS.HD_BACKGROUND_COLOR)

		# Draw border lines
		Scoreboard.drawBorders(self.header, SETTINGS.HD_BORDER_COLOR)
		# Draw column divider lines
		Scoreboard.drawColDivides(self.header, [self.div1_x, self.div2_x], SETTINGS.HD_BORDER_COLOR)

		# Draw header
		self.header.blit(self.font.render(SCORE_HEADER, True, SETTINGS.HD_TEXT_COLOR), (self.score_x, self.row_padding))
		self.header.blit(self.font.render(USER_HEADER, True, SETTINGS.HD_TEXT_COLOR), (self.user_x, self.row_padding))
		self.header.blit(self.font.render(DATE_HEADER, True, SETTINGS.HD_TEXT_COLOR), (self.date_x, self.row_padding))
	
	# Redraws the entire contents panel (contains only relevant scores)
	def redrawContents(self):
		# Clear
		self.contents.fill(SETTINGS.CT_BACKGROUND_COLOR)
		# Draw borders and dividers
		Scoreboard.drawBorders(self.contents, SETTINGS.CT_BORDER_COLOR)
		Scoreboard.drawColDivides(self.contents, [self.div1_x, self.div2_x], SETTINGS.CT_BORDER_COLOR)

		# Adjust rect values for positioning lines and such
		con_rect = self.contents.get_rect()
		bottom, right, left = con_rect.bottom-1, con_rect.right-1, con_rect.left

		# Initialize loop condition variables
		y = self.row_padding
		cnt = Scoreboard.getCnt()
		if self.reverse_order:
			i = cnt-1 - self.index
			i_inc = -1
		else:
			i = self.index
			i_inc = 1

		# Draw each row
		while y < bottom and 0 <= i < cnt:
			self.contents.blit(self.font.render(self.active_score_list[i].scoreStr(), True, SETTINGS.CT_TEXT_COLOR), (self.score_x, y))
			self.contents.blit(self.font.render(self.active_score_list[i].userStr(), True, SETTINGS.CT_TEXT_COLOR), (self.user_x, y))
			self.contents.blit(self.font.render(self.active_score_list[i].dateStr(), True, SETTINGS.CT_TEXT_COLOR), (self.date_x, y))
			y += self.line_height + self.row_padding
			pygame.draw.line(self.contents, SETTINGS.CT_BORDER_COLOR, (left, y), (right, y))
			y += self.row_padding
			i += i_inc



	### BEGIN STATIC COMPONENTS ###

	scores_by_score:SortedList = SortedList(key=sortScore)
	scores_by_date:SortedList = SortedList(key=sortDate)
	scores_by_user:SortedList = SortedList(key=sortUser)
	scores_loaded:bool = False
	
	def loadScores():
		if not os.path.exists(SB_DIR):
			os.makedirs(SB_DIR)
		files = os.listdir(SB_DIR)
		# Get all files in scoreboard directory
		for file in files:
			# If a scoreboard file (.sb)
			fl = len(file)
			if fl > 2 and file[fl-3 : fl] == ".sb":
				# If is actually a file (not a dir/folder)
				file_path = SB_DIR + file
				if os.path.isfile(file_path):
					invalids = []
					Scoreboard.__loadFile(file_path, invalids)
					Scoreboard.__archiveScores(invalids, file)
					
					# Remove any extra .sb files
					if file != SB_FILE:
						os.remove(file_path)
		Scoreboard.scores_loaded = True

	# Adds scores to each list (each list holds references to the same items, just sorted in a different order)
	def insertScore(score:Score):
		if score.valid:
			Scoreboard.scores_by_score.add(score)
			Scoreboard.scores_by_date.add(score)
			Scoreboard.scores_by_user.add(score)
		else:
			print("Invalid score:", score)


	def __loadFile(file_path:str, invalids:list[str] = -1):
		if invalids != -1: invalids.clear()

		with open(file_path, 'r') as file:
			line = file.readline().strip()
			# For each line (score)
			while line:
				# Genereate and append only if the score is valid
				score = Score(line)
				if score.valid: 
					Scoreboard.insertScore(score)
				else:
					print("Error: Score not valid {%s}" % line)
					if invalids != -1: invalids.append(line)
				# Get next line
				line = file.readline().strip()


	def __archiveScores(invalids:list[str], filename):
		# Archive invalid scores
		if len(invalids) > 0:
			print("Archiving")
			# Generate archive file path
			if not os.path.exists(ARCHIVE_DIR):
				os.makedirs(ARCHIVE_DIR)
			new_file = getNewFilePath(ARCHIVE_DIR + filename + 'a')

			# Write invalid scores to archive file
			with open(new_file, 'w+') as archive:
				for line in invalids:
					archive.write(line + '\n')


	def export():
		if not Scoreboard.scores_loaded or len(Scoreboard.scores_by_score) <= 0:
			print("No scores were loaded, skipping export...")
			return
		
		# Create a backup of the existing .sb
		main_file = SB_DIR + SB_FILE
		archive_file = main_file + 'a'
		if os.path.exists(main_file): 
			archive_file = getNewFilePath(archive_file)
			os.rename(main_file, archive_file)


		cnt = 0
		# Write a new .sb file
		with open(main_file, 'w+') as file:
			for score in Scoreboard.scores_by_score:
				file.write(score.__str__() + '\n')
				cnt += 1
		print("Exported %d scores" % cnt)
		
		# Delete temporary backup file
		if os.path.exists(archive_file): os.remove(archive_file)

	
	def getCnt(): return len(Scoreboard.scores_by_score)


	def toStr() -> str:
		s = ""
		for score in Scoreboard.scores_by_score:
			s += score.fullDetailStr() + '\n'
		return s
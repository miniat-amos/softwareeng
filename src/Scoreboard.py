import os
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

	def __init__(self, line:str) -> None:
		self.valid = True
		str_list:list[str] = line.split(' ')
		if len(str_list) < 3:
			self.valid = False
			return
		
		# Load score
		try:
			self.score:int = int(str_list[0])
		except:
			self.valid = False
			return
		
		# Load username
		try:
			username = NAME_FORM.match(str_list[1])
			self.username:str = username.string
		except:
			self.valid = False
			return
		
		# Load date
		try:
			self.date:datetime = datetime.strptime(str_list[2], DT_FORMAT)
		except:
			self.valid = False
			return

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

	def __init__(self, size:tuple[int,int], color = (255,255,255), font = -1, row_padding = 8, col_padding = 12) -> None:
		super().__init__()
		if not Scoreboard.scores_loaded: Scoreboard.loadScores()

		self.contents:Surface = 0
		self.header:Surface = 0

		self.color = color
		self.col_padding = col_padding
		self.row_padding = row_padding
		self.index = 0
		self.scroll_pos = [0,0]

		self.need_redraw_window = True
		self.need_update_contents = True
		self.old_scroll = [-1,-1]
		self.old_index = -1

		self.active_score_list = Scoreboard.scores_by_score
		self.reverse_order = False
		
		self.setFont(font)
	
	
	def update(self):
		# Prevent from scrolling below scoreboard
		dist_from_bottom = (Scoreboard.getCnt() - self.index + 1) * self.row_height - self.height - self.scroll_pos[1]
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
			print(d_index)
		
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
		
		# If scroll has changed, redraw window
		if self.scroll_pos[0] != self.old_scroll[0] \
			or self.scroll_pos[1] != self.old_scroll[1] \
			or self.index == self.old_index:
			
			self.need_update_contents = True
			self.need_redraw_window = True
		
		if self.need_update_contents:
			self.redrawContents()
			self.need_update_contents = False
			self.need_redraw_window = True

		if self.need_redraw_window:
			self.redrawWindow()
		
		self.need_redraw_window = False
		self.old_scroll = self.scroll_pos.copy()
		self.old_index = self.index


	def checkClick(self, global_pos:tuple[int,int]):
		if not self.get_rect().collidepoint(global_pos): return
		
		x = global_pos[0] - self.left
		y = global_pos[1] - self.top

		print("Clicked (%d, %d)" % (x, y))
		
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
	def scroll(self, down:bool):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
			axis = 0
		else:
			axis = 1
		
		if down:
			self.scroll_pos[axis] += SCROLL_AMOUNT
		else:
			self.scroll_pos[axis] -= SCROLL_AMOUNT

	def scrollUp(self): self.scroll(False)
	def scrollDown(self): self.scroll(True)


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


	def setFont(self, font):
		if font != -1:
			self.font:pygame.font.Font = font
		else:
			self.font:pygame.font.Font = pygame.font.Font(None, 24)
		self.calcDimensions()


	def calcDimensions(self):
		char_size = self.font.size('_')
		self.line_height = char_size[1]
		char_x = char_size[0]

		u_height, u_width = self.height-2, self.width-2

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
		extra_col_space = u_width - tot_content_width
		
		# If scores go off of scoreboard on right
		if extra_col_space < 0:
			con_width = tot_content_width
			head_width = tot_content_width

			self.left_padding = self.col_padding
			self.right_padding = self.col_padding
		# If scores fit on scoreboard
		else:
			con_width = u_width
			head_width = u_width

			self.left_padding = self.col_padding
			self.right_padding = self.col_padding + extra_col_space // 3
		
		content_rows = u_height // self.line_height + 5
		con_height = content_rows * self.line_height
		self.row_height = self.line_height + 2*self.row_padding
		self.contents = Surface((con_width, con_height), pygame.SRCALPHA)
		self.header = Surface((head_width, self.row_height), pygame.SRCALPHA)
		
		# Define x positions of column contents and dividers
		self.score_x = self.left_padding
		self.div1_x = self.score_x + self.score_w + self.right_padding
		self.user_x = self.div1_x + self.left_padding
		self.div2_x = self.user_x + self.user_w + self.right_padding
		self.date_x = self.div2_x + self.left_padding

		self.contents_bottom_right = (self.contents.get_width(), self.contents.get_height() + self.row_height)

		# print("<%d> %d <%d> %d <%d> |%d| lp=%d rp=%d" % (self.score_w, self.div1_x, self.user_w, self.div2_x, self.date_w, extra_col_space, self.left_padding, self.right_padding))
		self.redraw()


	def drawBorders(surf:Surface, col:tuple[int,int,int,int] = (255,255,255,255)):
		rect = surf.get_rect()
		right, bottom = rect.right-1, rect.bottom-1
		left, top = rect.left, rect.top
		pygame.draw.line(surf, col, (left, top), (right, top))
		pygame.draw.line(surf, col, (left, bottom), (right, bottom))
		pygame.draw.line(surf, col, (left, top), (left, bottom))
		pygame.draw.line(surf, col, (right, top), (right, bottom))

	def drawColDivides(surf:Surface, lines:list[int], col:tuple[int,int,int,int] = (255,255,255,255)):
		rect = surf.get_rect()
		top, bottom = rect.top, rect.bottom-1
		for line_x in lines:
			pygame.draw.line(surf, col, (line_x, top), (line_x, bottom))

	
	def redraw(self):
		self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
		self.redrawHeader()
		self.redrawContents()
		self.redrawWindow()

	
	def redrawWindow(self):
		self.surface.fill((0,0,0,255))

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


	def redrawHeader(self):
		self.header.fill((255,128,0,15))

		head_div_color = (255,128,0,255)

		# Draw border lines
		Scoreboard.drawBorders(self.header, head_div_color)
		# Draw column divider lines
		Scoreboard.drawColDivides(self.header, [self.div1_x, self.div2_x], head_div_color)

		# Draw header
		self.header.blit(self.font.render(SCORE_HEADER, True, self.color), (self.score_x, self.row_padding))
		self.header.blit(self.font.render(USER_HEADER, True, self.color), (self.user_x, self.row_padding))
		self.header.blit(self.font.render(DATE_HEADER, True, self.color), (self.date_x, self.row_padding))
	

	def redrawContents(self):
		# Clear
		self.contents.fill((0,192,255,15))
		# Draw borders and dividers
		con_div_color = (0,192,255,255)
		Scoreboard.drawBorders(self.contents, con_div_color)
		Scoreboard.drawColDivides(self.contents, [self.div1_x, self.div2_x], con_div_color)
		
		con_rect = self.contents.get_rect()
		bottom, right = con_rect.bottom-1, con_rect.right-1
		left = con_rect.left

		y = self.row_padding
		cnt = Scoreboard.getCnt()
		if self.reverse_order:
			i = Scoreboard.getCnt() - 1 - self.index
			i_inc = -1
		else:
			i = self.index
			i_inc = 1

		while y < bottom and 0 <= i < cnt:
			self.contents.blit(self.font.render(self.active_score_list[i].scoreStr(), True, self.color), (self.score_x, y))
			self.contents.blit(self.font.render(self.active_score_list[i].userStr(), True, self.color), (self.user_x, y))
			self.contents.blit(self.font.render(self.active_score_list[i].dateStr(), True, self.color), (self.date_x, y))
			y += self.line_height + self.row_padding
			pygame.draw.line(self.contents, con_div_color, (left, y), (right, y))
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
		Scoreboard.scores_by_score.add(score)
		Scoreboard.scores_by_date.add(score)
		Scoreboard.scores_by_user.add(score)


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
		# Create a backup of the existing .sb
		main_file = SB_DIR + SB_FILE
		archive_file = main_file + 'a'
		if os.path.exists(main_file): 
			archive_file = getNewFilePath(archive_file)
			os.rename(main_file, archive_file)

		# Write a new .sb file
		with open(main_file, 'w+') as file:
			for score in Scoreboard.scores_by_score:
				file.write(score.__str__() + '\n')
		
		# Delete temporary backup file
		if os.path.exists(archive_file): os.remove(archive_file)

	
	def getCnt(): return len(Scoreboard.scores_by_score)


	def toStr() -> str:
		s = ""
		for score in Scoreboard.scores_by_score:
			s += score.fullDetailStr() + '\n'
		return s


# If the desired filepath given already exists, modify until it's unique, return the first unique one
def getNewFilePath(desired_fp:str):
	while os.path.exists(desired_fp):
		dp = desired_fp.rfind('.')
		desired_fp = desired_fp[:dp] + '.' + desired_fp[dp:]
	return desired_fp
# Channel: updates  
## January-24-2024  
**@ 12:07:01 | From Josh**  
`2-camera` branch was merged into main  
  
**@ 17:07:12 | From Dylan**  
made "collision" branch. New "get_pos" method in player class gets where the player will be if allowed to move. Mask objects are made of the collision maps and the player, and if the future position from the get_pos method would make the masks overlap, the movement does not happen  
  
**@ 17:07:50 | From Dylan**  
Only problem is that right now no diagonal movement is allowed against a surface  
  
## January-25-2024  
**@ 19:19:50 | From Dylan**  
diagonal movement now lets you slide along a wall, commit messages on my collision branch explain how  
  
**@ 19:28:09 | From Dylan**  
Should i just merge this into main now so that there is less confusion when you add your features from branches?  
  
**@ 08:56:18 | From Michael | Replying to Dylan: "Should i just merge this into main now s..."**  
Hmm, I don't see a reason not to, but I don't see anything wrong with leaving it as-is till Monday when we can decide how to test/review each other's code.  
  
**@ 08:58:45 | From Michael**  
Also, I started a branch called "PlayerClass" where I started working on class for players. I made some progress last night but it's still a WIP  
  
**@ 09:02:30 | From Dylan**  
wasnt the code review stuff not really until the 3 cycles?  
  
**@ 09:03:38 | From Michael**  
I mean we still need to know what everyone else is doing and understand their code a bit, even if it's not formal testing/reviewing  
  
**@ 09:03:45 | From Dylan**  
ok  
  
## January-29-2024  
**@ 00:18:16 | From Josh**  
Got some basic UI for an HP stat up on my branch. Just pushed to that branch.   
  
Going to flesh it out a bit more in the morning! I'd like to add a 'loot' stat for UI and add visual bars to show for HP  
  
**@ 09:58:53 | From Dylan**  
Thanks for doing that! Should we use an hp bar or would hearts be better for a simpler game like this?  
  
**@ 09:59:14 | From Josh**  
Hearts would be cool!  
  
**@ 10:34:41 | From Josh**  
hearts added! Pushing now!  
  
**@ 13:47:47 | From Josh | Created a Thread**  
Ui updates  
  
**@ 16:41:14 | From Dylan**  
I made the collision sounds and coin spawns. I realized when I was going to make picking up a coin increase a number in the player object, I think we forgot to take the updated player class in the PlayerClass folder and actually apply it to the main root player class  
  
## February-03-2024  
**@ 13:20:43 | From Josh**  
I've got a pretty solid menu system working! I'm going to merge it with the main branch since there aren't any conflicts. Here's a photo.  
  
**@ 13:21:31 | From Josh**  
Merged!  
  
**@ 13:48:58 | From Josh**  
Note that there is a bug right now that makes it annoying to close the game... hitting the 'x' in the upper right hand corner does not always work  
  
**@ 14:39:54 | From Michael**  
Ooh nice! Looks good, and I like the music!  
  
**@ 14:41:35 | From Josh**  
Thanks!!!  
  
## February-04-2024  
**@ 19:11:50 | From Dylan**  
I did some work on the lightning bolt but it's not quite the prettiest. It doesn't really line up the best with targeting the player; I fixed the targeting a bit but I kinda figured that it might be best if i wait for the entity superclass so that i can work off that  
**Reactions:** 👍  
  
**@ 19:20:30 | From Dylan | Replying to Josh: "I've got a pretty solid menu system work..."**  
also this is really nice  
  
**@ 19:23:11 | From Josh | Replying to Dylan: "also this is really nice..."**  
Thanks!  
  
## February-05-2024  
**@ 10:05:57 | From Michael**  
I'm a bit late to the party but I finished up my work last night. I cleaned up the rendering stuff, fixed some bugs with it, added the (non-functional) pawn shop, etc.  
  
 I also made a super basic loot class. It doesn't support different types of loot atm, but it keeps track of how much a piece of loot is worth and draws heart.png as a placeholder sprite.   
  
All of it is on the BasicRooms branch  
  
**@ 10:31:46 | From Josh**  
Nice!!  
  
**@ 10:32:00 | From Josh**  
I didn’t get to the Entity class but I’ll have time to wrap my portion up today  
  
## February-06-2024  
**@ 21:48:30 | From Dylan**  
Looking at adding collision for the new system but i dont really know how to make it work  - since all the houses and their rects are inside of a render group it's not easy to access an individual one (or a potential mask for it) directly, meaning im not sure how to make a call for the player to check whether a move would make it overlap with a desired mask  
  
**@ 21:51:27 | From Dylan**  
The thing with the roof checking to see if it overlaps with the player is easy bc theres only one player mask for each roof to keep track of, but the player needs to somehow either check all of the map collision masks or figure out exactly which collision map(s) to check  
  
**@ 12:01:52 | From Michael**  
Sorry, my code isn't terribly readable, and I had to do some funky stuff to get it to work properly.   
  
If you want, I can write a function that (when called from the map object) will run for each tile/building that the player might be interacting with, then you should be able to add your own collision checks to this function.   
  
Or we can try to figure it out together before/during CS450 later today, either way is fine with me.  
  
**@ 12:03:49 | From Dylan**  
yeah i got some work to do rn, if i have time i will keep looking at it before 450 then i will talk to you during it  
  
**@ 12:38:20 | From Michael**  
Alright sounds good to me  
  
**@ 16:09:17 | From Michael**  
On main, I just added a function Map.checkInteractions(), which calls checkInteractions() on every part of the map the player may be trying to interact with. For collisions, loot-pickup, or other interactions, you should be able to add that code to the correct class's .checkInteractions()  
  
The code I wrote was definitely very confusing, so I'll need to do better about communication & collaboration in the cycles. Worst case scenario I should be able to help either of you merge your own code in without having to redesign/break either of our stuff.  
  
**@ 16:36:22 | From Dylan**  
Since we're almost done with this cycle and i dont think confer would want us to spend a ton of time reinventing the same stuff, do you think it might be a good idea if for now i just make it so the player cant walk past the left and right "sections" of the screen (past the line where the building fronts are)?  
  
**@ 17:10:09 | From Michael**  
Honestly that sounds like the simplest solution, the only problem is that I drew the pawn shop in a slightly different size than the other buildings, but that's a super simple fix on my end, so if you wanna do that just ignore the pawn shops (brick buildings) and I'll fix the size.  
  
## February-07-2024  
**@ 21:09:18 | From Dylan**  
Is there any good way to get the room object that the player is currently in?  
  
**@ 21:10:26 | From Dylan**  
Im pretty sure the map.room_list[map.getplayerroom] doesnt actually get the room the player is in  
  
**@ 21:11:23 | From Dylan**  
Or do you know at least what the index of the starting room is or usually is  
  
**@ 21:14:37 | From Dylan**  
I might be wrong but the problem with using the checkInteractions function or other stuff like that (basically the concept of the map class being what's running the processes) is that idrk how to actually access stuff or run new processes in the main class  
  
**@ 21:16:01 | From Dylan**  
i kinda was able to make just a couple masks to try to use for collisions by just using tile[0] in room[0] but i dont actually know which room or tile that is  
  
**@ 21:20:31 | From Michael**  
getPlayerRoom() essentially returns the room the player is in based on what's being rendered, so yea it's not the actual index in the list. Just double checked and (self.getPlayerRoom() + self.render_start) will return the index of the room that the player is in.  
  
**@ 21:23:16 | From Michael**  
From there if you wanted to check what tile the player is in, you should be able to find that from the player's position and the tile's position now that you have the room the player is in. Just loop through the tiles and compare positions. Positions of tile and player are stored in (player/tile).rect  
  
**@ 21:25:58 | From Dylan**  
do you know which tile is tile 0 (bottom? top? Ive been trying to check but i cant tell which it is)  
  
**@ 21:26:30 | From Michael**  
Tile 0 should be the top, which means lowest y value since pygame is kinda backwards  
  
**@ 21:26:40 | From Michael**  
Same with rooms, I tried to make sure that part was consistent at least  
  
**@ 21:29:03 | From Dylan**  
ok yeah thats right, idk how i wasnt seeing that ig i was just confused  
  
**@ 21:29:49 | From Michael**  
Nah all good, it's an easy thing to miss  
  
## February-08-2024  
**@ 19:29:56 | From Dylan**  
any good way to tell when the player has moved to a different room?  
  
**@ 19:37:19 | From Michael**  
Not really, you just have to check if the player's room number has changed but that's about it  
  
**@ 20:00:20 | From Dylan**  
that doesnt really work because after you go up like 4 rooms the player room will always be either 3 or 4 according to the getplayerroom function  
  
**@ 20:00:38 | From Dylan**  
I would just go with what i have now because it works well enought but it runs pretty badly  
  
**@ 20:32:06 | From Dylan**  
Ok so unless we figure out a way to determine when the player's room has changed (which could be used to update the collision maps only in a new room, not on every frame), i think im done for the most part. Press L to summon a lightning bolt. Press and hold M to show the player's collision map and the building collision maps. Press and hold N to show the roof collision maps, which the lightning bolt target cannot follow you under.  
  
**@ 20:32:20 | From Dylan**  
This is on the "new_lightning" branch  
  
**@ 20:34:49 | From Dylan**  
if either of you have an idea for how to flag when the player's room has changed, you can replace the "if (True)" line in the main file with that flag  
  
**@ 21:27:01 | From Michael**  
Awesome sounds good, I'll take a loot at it at some point to see if there's a good solution, but if it works then that's all that really matter  
  
## February-10-2024  
**@ 20:53:10 | From Michael**  
Made a quick commit (on a new branch to be safe) optimizing some of the lighting/collision code in main.py. Everything should work the same, I mostly just removed a couple of extra draws that didn't need to be there.  
  
**@ 22:12:10 | From Dylan**  
Wow thanks for doing that. I went on the branch and added a few things  - the lightning bolt collision was using the wrong collision map, so i switched it to the roof map. Also I added back in the visualized collision maps when pressing M or N because i think they're kinda cool  
  
**@ 23:08:31 | From Michael**  
Yeah no problem, and good catch, didn't notice that before  
  
**@ 23:08:40 | From Michael**  
Also, happy birthday!  
  
**@ 09:18:44 | From Dylan**  
Thanks i appreciate it!  
  
## February-11-2024  
**@ 14:46:10 | From Michael**  
Simple last-minute update: Needed to switch the loot's sprite from heart to coin, and realized it only took 10 or so lines of code to make lightning damage players and loot be collectable, so I did that really quick. Kind of janky how it works, but should make for a slightly better demo.  
  
## February-12-2024  
**@ 20:58:33 | From Dylan**  
Oh thanks for that too!  
  
## February-15-2024  
**@ 19:12:10 | From Dylan**  
would yall prefer for the player's coordinates to be its top left or the center of its rectangle?  
  
**@ 19:20:12 | From Dylan**  
ig it doesnt really matter bc thats just the starting location and you can get the center/topleft coords from the rect later anyways  
  
**@ 19:27:59 | From Michael**  
I feel like if center is the most intuitive, but yeah because of how rects work it shouldn't matter too much  
  
## February-19-2024  
**@ 17:16:04 | From Michael**  
@Josh I finished the basics of the map rendering and pushed it to the 10-Map branch, feel free to merge into main if you need.  
  
## February-20-2024  
**@ 19:51:47 | From Josh | Replying to Michael: "<@544680424954134533> I finished the bas..."**  
Great! I'll take a look tonight or tomorrow  
  
## February-21-2024  
**@ 09:41:13 | From Josh**  
i've largely integrated a new camera with the map. I need to collaborate with Michael during class today to figure out the "drawoffset"  
  
**@ 10:38:58 | From Josh**  
Just pushed the button feature  - should be ready for testing  
  
**@ 11:55:38 | From Josh**  
I lied, I want to add two more things to buttons before testing  
  
## February-22-2024  
**@ 10:35:37 | From Dylan**  
player is merged with map in the 15-player-map branch  
  
## February-24-2024  
**@ 12:42:52 | From Dylan**  
I'm mostly done with my stuff for the weekly status report, i wrote my accomplishments and my hours are written at the bottom  
  
**@ 12:43:53 | From Dylan**  
I would just put my hours on the chart now but i didn't yet so that we can add them at the end and don't lose track of what we already added/didn't add  
  
**@ 12:44:05 | From Dylan**  
also we gotta write next week's objectives  
  
**@ 12:52:07 | From Michael**  
Alright gotcha, sounds good. I haven't been able to do much work yet this week, but I'll be spending a good chunk of today working on Town so I'll add my progress once I make it.  
  
**@ 12:52:29 | From Michael**  
I'll try to think of some obejctives as well. Off the top of my head I'd say creating a sound effects feature, creating a loot feature, and testing the player.  
  
**@ 13:16:02 | From Dylan**  
Ok  
- Perform code review on World (Map)  
- Perform testing on Player  
- Complete code for Lightning  
  
**@ 13:16:14 | From Dylan**  
plus stuff for your other features  
  
## February-25-2024  
**@ 09:38:22 | From Dylan**  
Oh wow thanks michael for working on collision stuff between player and town, i figured i would do that but it looks like you mostly already got it  
  
**@ 11:16:12 | From Dylan**  
we gotta write down the testers for town and menus  
  
**@ 11:16:20 | From Dylan**  
can i do the testing for town?  
  
**@ 11:16:58 | From Michael**  
Sure that's fine with me, I'll do testing for menus then  
  
**@ 13:54:50 | From Josh**  
Hey! I'm going to wrap up my TitleScreen and then work on a Sound / Music Manager  
  
**@ 13:57:49 | From Michael**  
Alrighty sounds good  
**Reactions:** 👍  
  
**@ 14:05:16 | From Dylan**  
Ok one of us needs to submit by 5 (even tho it's listed on d2l as midnight but i think the paper says it's always 5)  
  
**@ 14:05:42 | From Dylan**  
If I'm not the one to submit, my hours are listed at the bottom to add to the chart  
  
**@ 14:06:08 | From Michael**  
I can submit it this week  
  
**@ 14:06:25 | From Josh**  
I'm going to add my stuff momentarily :D  
  
**@ 14:06:45 | From Michael**  
Also, the due time is different for some reason, so we have until midnight if needed.  
**Reactions:** 👍  
  
**@ 14:08:14 | From Michael**  
Alright so I'll send a msg by like 4:30 ish if it looks like anything's missing, then I'll submit it a bit later. Lmk if any of you need more time to add to it or fill things out  
**Reactions:** 👍  
  
**@ 14:10:05 | From Dylan**  
ok  
  
**@ 14:54:56 | From Josh**  
Okay I've pushed my changes to `12-titlescreen` and updated the weekly team status report  
**Reactions:** 👍  
  
**@ 15:44:21 | From Dylan**  
are both of your hours filled out?  
  
**@ 15:45:31 | From Michael**  
Yup I filled mine out  
  
**@ 15:57:04 | From Josh**  
I believe so  
  
**@ 16:08:38 | From Dylan**  
i think some of our numbers might be messed up because of the combination of map and camera, it was 6.25 hrs total at the end of last week so if you did more than 1.75 hrs total lmk or change it pls  
  
**@ 16:11:24 | From Michael**  
It was mostly finished by the end of last week so I think that's accurate. That 1.75 hours was from testing, and then some tweaking I had to do to make it work with Town.  
  
**@ 16:34:13 | From Michael**  
Okay I added Dylan's hours, added a quick accomplishment for Josh's buttons/titlescreen, reworded a couple things here and there. Both of you just ping me whenever you're ready to submit it.  
  
**@ 16:40:26 | From Dylan**  
my stuff is done  
  
**@ 16:40:47 | From Dylan**  
josh did you do any test writing or anything else to write?  
  
**@ 16:40:57 | From Dylan**  
did you log the camera work you did under world?  
  
**@ 16:48:45 | From Dylan**  
@Josh  
  
**@ 16:59:48 | From Dylan**  
i submitted it since he generally wants them by 5. if you have changes then resubmit it  
  
**@ 17:36:41 | From Josh | Replying to Dylan: "josh did you do any test writing or anyt..."**  
I did test writing for the title screen  
  
**@ 17:37:07 | From Josh | Replying to Dylan: "did you log the camera work you did unde..."**  
I thought we combined Michael and I’s work under world?  
  
**@ 17:37:52 | From Dylan**  
yeah i just meant didnt you spend a few hours on that camera this week that you didnt add to the page yet?  
  
**@ 17:41:21 | From Josh**  
I thought I logged my time with the “world” feature  
  
**@ 17:49:05 | From Dylan**  
do you know how many hours it was? because michael said he spent like 1.75 hours on it, which i had thought accounted for the entire increase (aside from my stuff)  
  
**@ 17:49:41 | From Josh**  
I spent probably 3 hours on the camera  
  
**@ 17:50:00 | From Dylan**  
im not trying to keep bothering you with this stuff its just that we have less hours than i think confer expects so im trying to make sure there are no mistakes  
**Reactions:** 👍  
  
**@ 17:51:59 | From Dylan**  
looking at the version history i dont see any hours added from you except on the menus. so i think we can probably add those 3 hours to map since they dont seem to be logged under you  
  
**@ 17:52:23 | From Josh**  
Ah ok my mistake  
  
**@ 17:53:18 | From Dylan**  
next week should we just write our hours for each of us then add them at the end like i did this week? i dont want to make you do that but i did it to avoid confusion like this  
  
**@ 17:55:24 | From Josh**  
Yeah sure  
  
**@ 18:01:00 | From Michael**  
Yup sounds good to me too  
  
## February-27-2024  
**@ 13:43:27 | From Michael**  
Just tested the titlescreen, but the options menu is missing a "Back" button to return to the titlescreen. It passed everything else though.  
  
**@ 13:44:01 | From Josh | Replying to Michael: "Just tested the titlescreen, but the opt..."**  
I can add that back button tonight  
  
**@ 13:44:33 | From Michael**  
Alright sounds good, no rush. The testing for titlescreen only takes a few minutes anyways.  
  
**@ 17:27:44 | From Dylan**  
michael lmk if/when you want to combine lightning and town  
  
**@ 17:27:54 | From Dylan**  
or just do it if you want  
  
**@ 17:32:38 | From Dylan**  
also if we're gonna start loot/sound features, who should do what for those  
  
## February-28-2024  
**@ 20:45:54 | From Michael | Replying to Dylan: "michael lmk if/when you want to combine ..."**  
I can probably handle most if it myself once you've got lighting finished, but some help would probably be good, so I'm thinking we should work on that together for a bit tomorrow.  
  
**@ 20:46:23 | From Dylan**  
k  
  
**@ 20:47:30 | From Michael | Replying to Dylan: "also if we're gonna start loot/sound fea..."**  
I've never done sound before and loot would be pretty closely integrated with World/Town so I'd probably take loot, but I think most of the work should be saved for cycle 2 anyways so all I'd do for now is make the documentation.  
  
**@ 09:26:44 | From Dylan**  
Idk if I'm gonna be there today i aint feeling so great  
  
**@ 09:27:36 | From Josh**  
No worries! Get some rest :)  
  
**@ 10:08:29 | From Michael**  
Ahh sorry to hear that, feel better soon  
  
**@ 13:28:02 | From Josh**  
UI is made and ready for testing   
  
I've assigned the testing to @Dylan for now. Whenever you're feeling better, feel free to take a look. We can also send it over to Michael if needed too!  
  
## February-29-2024  
**@ 12:48:55 | From Dylan**  
i wrote a test suite for ui and added some test things to the description as constraints but i feel like the test suite is still kinda short  
  
**@ 13:09:13 | From Dylan**  
testing done, all of them passed but i will redo/do the extra tests if i come up with any more or either of you suggest something  
  
## March-01-2024  
**@ 11:05:19 | From Dylan**  
im looking at the town and seeing how the fully destroyed roofs have collision so you cant go under them, but im wondering how will we get the player out from under there when the roof is destroyed  
  
**@ 11:05:44 | From Dylan**  
i was thinking you could still go under the roof but it just wouldn't protect you, or it would just be completely gone  
  
**@ 11:06:50 | From Michael**  
Oh yeah didn't think much off it before because it wasn't really decided what a broken roof would do. I'll change it so that it doesn't protect the player but they can still go under it.  
  
**@ 11:19:20 | From Dylan**  
ok ik you were gonna do the lightning merging stuff but i wanted to help with some of it since ik the town thing is so big anyway, so in branch temp-town-lightning i think the merged stuff seems to be working  
  
**@ 12:07:03 | From Dylan**  
@Michael Ok so it's ugly but the game now recognizes when a lightning bolt is colliding with a roof. Idrk how to make the roof actually show the new damage but it does call updateBurnState on the roof and print a string showing that there is a collision happening. we will need to change it a little so it only does that when the lightning is striking, but i hope this helps with getting the basic functionality down  
  
**@ 12:08:27 | From Dylan**  
maybe we should just have the lightning class store a reference to map. that way it will have both the map and the player (sent in the lightning.update call) so when it strikes it can use both the map and the player to damage roofs and only damage the player if they aren't under an intact roof  
  
**@ 14:06:19 | From Dylan**  
actually we could just put that in the lightning strike() method, first check if there is a roof collision and then only check to damage the player if the roof was not damaged  
  
**@ 14:59:09 | From Michael**  
Alright cool, now that you got lighting working with town I can handle making the roofs functional. And yeah I'll make sure to include the roof checks in the lighting.strike() function, that seems like the most sensible way to do it.  
  
**@ 15:29:20 | From Dylan**  
what is the difference between roof_state and burn_state  
  
**@ 15:47:15 | From Michael**  
I mean I don't think I'm supposed to tell you low-level details since you're the tester for Town.  
  
**@ 15:47:33 | From Michael**  
The majority of the code left is for town specifically anyways so I can handle it.  
  
**@ 15:47:37 | From Michael**  
Also mb, I forgot to mention it yesterday but I finished the testing for Lighting, so that should be officially complete now.  
  
**@ 16:03:52 | From Dylan**  
oh sorry abt that i just did some more to basically make it fully work  
  
**@ 16:04:49 | From Dylan**  
i kinda for some reason read your message as like, for me to work some more on the lightning stuff and you could do some with the roofs but i ended up just kinda doing it  
  
**@ 16:06:28 | From Dylan**  
didn't mean to take your stuff from you but i wanted to see if i could figure out some more lightning stuff  
  
**@ 16:08:24 | From Michael**  
Nah it's all good, as long as it works in the end  
  
**@ 16:09:57 | From Dylan**  
ok it's kinda cobbled together too so you could still look at it and fix it/make it better if you were planning to do more this week  
  
**@ 16:10:27 | From Michael**  
Alright sounds good to me, it looks pretty good so far though  
  
**@ 18:00:22 | From Michael**  
Looked through it and made a couple small changes, but it looked pretty good so it was mostly moving things around and adding comments. I think this means Town is done and ready for testing.  
  
## March-02-2024  
**@ 11:45:04 | From Dylan**  
the tests passed, although i added back in 2 things: the out of bounds collision check in player, and you removed the 2 lines where the lightning actually does damage to the player so i put that back in  
  
**@ 11:46:16 | From Michael**  
Oh sorry about that, mb. Thanks for fixing it though.  
  
**@ 11:46:33 | From Dylan**  
No problem it's fine it was just kinda funny lol  
  
**@ 11:47:42 | From Dylan**  
I also added a file for general settings like screen size so that you can just include that file to access stuff like that (for example you need the screen size for the collision out of bounds thing but I didn't want to require/include sending the actual map into collision)  
  
**@ 11:48:13 | From Michael**  
Ooh okay nice, sounds good  
  
**@ 11:48:40 | From Dylan**  
oh also i made the buildings not randomly spawn on fire ofc  
  
**@ 11:48:57 | From Dylan**  
unless that was intended to stay that way but i assumed not  
  
**@ 11:48:57 | From Michael**  
Oh yeah I mostly did that for testing and never turned it off  
  
**@ 11:49:06 | From Michael**  
Nah just testing lol  
  
## March-05-2024  
**@ 21:21:48 | From Michael**  
@everyone Sorry to bug yall, but I think I've finished going through all the documents for our features and making sure they had consistent formatting. I'm going to print everything at around 5pm tomorrow, so before then, try to give everything a brief overview and make sure there isn't anything you want to add or change to any of the documents.  
**Reactions:** 👍  
  
**@ 21:24:05 | From Dylan**  
k thanks for going over the stuff  
  
**@ 21:24:09 | From Dylan**  
and for printing  
  
**@ 21:24:18 | From Michael**  
Also @Josh , I made a couple comments on the Sound and Music Manager description. I didn't want to make any changes without talking about it with you, so if you could look at those comments and lmk what you think or just make whatever adjustments you feel are best then that would be helpful. No rush though, pretty much anytime tonight or tomorrow.  
  
**@ 21:24:40 | From Michael | Replying to Dylan: "k thanks for going over the stuff..."**  
Yeah no problem, it's wasn't too hard or anything, just a bit annoying lol  
  
**@ 21:24:42 | From Josh | Replying to Michael: "Also <@544680424954134533> , I made a co..."**  
Sweet thanks for the feedback, it’ll be the first thing I work on tomorrow morning  
**Reactions:** 👍  
  
**@ 10:57:04 | From Josh**  
Music, Title Screen, and UI are now all integrated and demo-ready!!  
  
**@ 10:57:16 | From Josh**  
Going to make a demo video as a backup right now  
  
**@ 10:57:36 | From Josh**  
^Or we just use a video demo so that we know for certain how much time the demo will take 🤷‍♂️  
  
**@ 11:05:23 | From Josh**  
ACTION: Type = default  
  
**@ 11:05:30 | From Josh**  
Thoughts on this demo video?  
  
**@ 11:05:40 | From Josh**  
And were there any features we want to show off that I missed?  
  
**@ 11:15:26 | From Josh | Replying to Michael: "Also <@544680424954134533> , I made a co..."**  
Resolved those comments and added a volume changer via the up/down keys  
**Reactions:** 👍  
  
**@ 11:20:47 | From Dylan**  
i might actually change the lightning to only spawn in the direction the player is walking bc i made it either spawn 50% chance in front or behind the player but if it spawns behind it will just not show up basically, as seen in the video  
  
**@ 11:21:16 | From Josh | Replying to Dylan: "i might actually change the lightning to..."**  
Ok gotcha! If/when you make those changes just lemme know so I can rerecord the video  
  
**@ 11:22:04 | From Dylan**  
also that way you could point out you could technically turn backwards every second to manipulate the lightning into spawning behind you which is the kind of hidden gimmick confer seems to like  
  
**@ 11:33:52 | From Dylan | Replying to Josh: "Ok gotcha! If/when you make those change..."**  
ok it's fixed  
  
**@ 11:59:01 | From Michael | Replying to Josh: "And were there any features we want to s..."**  
Nothing major, but if you do need to redo the video to include Dylan's changes anyways, then make sure to show that the burnt down roofs won't protect the player from lighting.  
**Reactions:** 👍  
  

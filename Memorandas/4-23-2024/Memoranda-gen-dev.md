# Channel: gen-dev  
## January-24-2024  
**@ 00:33:29 | From Josh**  
Welp no time like the present to do this camera work! 💀  
  
**@ 10:16:45 | From Josh**  
Just wrapped up getting a camera to work  
  
**@ 10:16:58 | From Josh**  
It's on my branch, but Ill wait until class to merge that with y'all  
  
## February-05-2024  
**@ 14:38:27 | From Michael**  
Just a heads up, made a quick commit to main to add comments to my code. Most of it was late-night foggy-brain coding so I wasn't commenting much before lol  
**Reactions:** 👍  
  
## February-09-2024  
**@ 15:36:59 | From Michael**  
I was looking through the proposal, and I added a bit more detail to the "ABC Strategy," but I also saw a couple of things that I feel like should be shifted around or added.  
  
I feel like out current plan for the 3 cycles leans a bit too heavily towards the final one. Between all the stuff listed, plus last-minute cleanup and combining of code before presenting, on top of finals for other classes, I feel like the last cycle could get a bit overwhelming.  
  
I think we should shift collisions to the first cycle (it definitely won't be as hard as it was in the spike if we properly plan it out), and shift lightning to the second cycle. Or instead, we could have an unwritten plan that we'll try to stay at least one step ahead for the first cycles.   
  
Also, I think creating some kind of naming convention for code might be helpful, e.g. any programs used for testing will be named something like "test\_{feature}.py", example code will be named "example\_{title}.py", etc. That way as we develop, we can tell what is a class, what was just used for testing, and what still has example code that we'll need to reference later.  
  
**@ 15:41:30 | From Michael**  
Let me know if you think that sounds good then I can add it to the proposal, or if you disagree I'll just leave it as-is, either way is good with me.  
**Reactions:** 👍  
  
**@ 16:21:31 | From Josh | Replying to Michael: "I was looking through the proposal, and ..."**  
Cool! This works with me  
  
**@ 16:21:50 | From Josh**  
After those changes, I think our report is ready :D  
  
**@ 16:22:10 | From Josh**  
Things to bring Monday:  
- The report  
- Our printed peer evals  
- Our presentation  
  
**@ 16:22:35 | From Josh**  
I'll have local copies of the presentation on my laptop  
  
**@ 16:22:45 | From Josh**  
do we want to bring a video demo just in case our live demo fails?  
  
**@ 16:23:00 | From Josh**  
and who's laptop are we planning on using to present? (Michael's?)  
  
**@ 16:31:38 | From Josh**  
^ also I did clean up the report a bit  
  
**@ 16:51:30 | From Michael**  
Alright nice! And yeah, I definitely think a video would be good, I can handle that part though. And my laptop is probably the safest bet, but we should probably each be prepared to use our own laptop in a worst-case-scenario.  
  
**@ 17:02:33 | From Josh**  
👌  
  
## February-10-2024  
**@ 22:13:39 | From Dylan**  
I have my peer evaluation printed, we will just need the printed proposal  
  
## February-11-2024  
**@ 14:47:02 | From Michael**  
Couldn't remember if it was decided who was printing the proposal, but I have a printer so I'll print a copy for tomorrow just in case.  
  
## February-12-2024  
**@ 20:59:14 | From Dylan**  
Ok i appreciate it. Make sure each of you has yours done and printed as well  
**Reactions:** 👍  
  
## February-14-2024  
**@ 16:00:46 | From Dylan**  
I realized I might have been getting ahead of myself thinking about collision already. Would it be better for me to work on a player class instead for now?  
  
**@ 16:03:39 | From Michael**  
Yeah that's probably a better place to start for now  
  
**@ 16:37:57 | From Dylan**  
Just a note for now, but I'm not really sure what is best to include in the player feature description. Currently I have the constraints that the player should take damage from lightning, collide with walls, etc but those sound like features that might be better put in other features, but they still pertain to the player. I might break it down into subfeatures like says in the MVPP slides but we can figure that out later ig  
  
**@ 17:23:57 | From Michael**  
Hmm, now that I've given in some thought, I'm kinda confused too. For now I feel like focusing on what a feature has as a lone entity is probably best (e.g. "player has health count and 'inventory'"), but I think I'll try to talk to confer about it tomorrow at his office hours to get it straightened out.  
  
**@ 17:24:54 | From Michael**  
Actually since it's constraints you were talking about and not subfeatures, maybe what I was saying about "player has health" etc. doesn't really make sense  
  
## February-15-2024  
**@ 12:23:02 | From Michael | Replying to Dylan: "Just a note for now, but I'm not really ..."**  
I just talked with Confer about it, and got some clarity on how the feature definitions and constraints work.  
  
We only need to define a feature's interactions with features that are already developed, and *can* with features that are being developed along side it. Currently, Player is the only feature in existence, so we don't need to mention lighting, collisions, loot, etc. The Player constraints should be very simple, e.g. "Player can't move offscreen horizontally", and *maybe* "game ends when player's health reaches 0".    
  
When we develop a feature that interacts with Player (e.g. Lightning), we'll staple on any relevant constraints to the new feature (e.g. Lightning: "lightning must damage player"), and can leave the Player feature as-is. Basically, if it hasn't been developed and you're not working on it, save it for later.   
  
Confer also said that animations are very simple, so we should probably include that in the player feature, but I can help with that since I did that last time. Or, if I make an animation class that works for all renderable things, I could probably argue that it's a feature so we don't have to worry about it yet.  
  
**@ 12:24:24 | From Dylan**  
Ok i should try to put like an hour or 2 more into this so i can try to figure out animations  
  
**@ 12:28:27 | From Michael**  
Alright sounds good  
  
## February-18-2024  
**@ 21:28:27 | From Dylan**  
One of us has to submit the weekly team status report by tomorrow at 5, it's posted on brightspace  
  
**@ 21:28:40 | From Dylan**  
I'm pretty much done with my part  
  
**@ 21:31:09 | From Michael**  
I can handle submitting the report if you want, I'm mostly done as well  
  
**@ 12:22:51 | From Michael**  
I'll upload the report at around 4pm today to be safe, so if anyone wants to make changes to it, be sure to make them by 4.  
  
**@ 14:51:43 | From Dylan**  
i spent like 15 minutes writing (i mean literally writing in text) a couple test suite things for the map, so i will add .25 to map hours  
  
**@ 14:52:34 | From Dylan**  
@Josh sorry to @ you but did you do anything yet? we have to submit by 5  
  
**@ 15:45:27 | From Josh | Replying to Dylan: "<@544680424954134533> sorry to @ you but..."**  
Yes! I did 2 hours of work… had a bit of a family emergency and had to go home. I started a camera class  
  
**@ 15:45:42 | From Josh**  
I don’t have a laptop :(  
  
**@ 15:46:01 | From Josh**  
Also ping me whenever you need to! I usually don’t check discord unless I’m pinged  
  
**@ 15:52:49 | From Dylan**  
No worries I totally understand. Don't worry about anything here if anything serious like that ever happens  
**Reactions:** ❤️  
  
**@ 15:53:33 | From Dylan**  
Also not to tell you what to do but maybe mention something about that in the report so confer knows and doesn't question us?  
  
**@ 15:54:28 | From Dylan**  
only if you now have time that is ofc  
  
**@ 15:56:17 | From Josh**  
Yes will do! I don’t have a laptop to add to the report atm  
  
**@ 15:57:13 | From Dylan**  
do you want one of us to type something for you?  
  
**@ 16:37:15 | From Dylan**  
@Josh are you good with this  
  
**@ 16:38:00 | From Josh**  
Yes  
  
**@ 16:38:47 | From Dylan**  
ok i will submit this  
  
**@ 16:46:59 | From Dylan**  
submitted and made a copy for next week  
  
## February-20-2024  
**@ 12:38:38 | From Dylan**  
just fyi the map test suite i wrote is for both the map and camera since confer said we should combine them  
  
**@ 12:39:53 | From Dylan**  
also rn im not really sure what to work on since the player functionality is pretty much done, i would work on collision between player and map but the map doesnt have buildings yet and since there isnt a camera the map doesnt really visually work with the player  
  
**@ 12:40:03 | From Dylan**  
should i start some work on lightning?  
  
**@ 12:59:59 | From Dylan**  
one other thing: we might want to merge the Button feature that's onto the google drive into some UI or Menu functionality (maybe with the title screen?) since just a button to use for various menus isn't really a user focused feature  
  
**@ 13:00:27 | From Dylan**  
on a similar note i might just consolidate collision into the player stuff since i already made some functionality for it  
  
## March-03-2024  
**@ 15:11:53 | From Michael**  
I went through the report and added all of your hours. I also added our code reviews as one of the objectives, and reworded the risk since I had worded it pretty poorly last time. I think it's just about good to go, so once both of you think it's ready one of us can submit it. I'd assume Dylan will submit it since he's been doing that, but I can if needed. ( @Josh  @Dylan )  
  
**@ 15:12:52 | From Josh**  
Ok sweet  
  
**@ 15:16:29 | From Dylan**  
Ok I think my content should be done, I'm just not sure if the risk thing is worth keeping there in case he doesn't like how it's worded or he doesn't want there to be a risk at the end of the cycle idk  
  
**@ 15:19:50 | From Michael**  
Hmm, I feel like it would be worse to remove a risk without resolving it, and it's not something that will cause issues for the end of this cycle so I think it's okay. I could be wrong, but that's the way I see it at least.  
  
**@ 15:47:47 | From Dylan**  
ok you're probably right  
  
**@ 16:14:22 | From Dylan**  
I turned in the weekly thing  
  
**@ 16:15:48 | From Dylan**  
I submitted a separate copy without the individual hours so that we still have the individual hours on our copy  
  
**@ 16:48:16 | From Michael**  
Awesome sounds good  
  
## March-04-2024  
**@ 14:36:07 | From Dylan**  
It looks like we need a "version description" to include with our deliverables for the software development section  
  
**@ 18:35:50 | From Dylan**  
Actually the user manual basically has a version description in it. Should we split that off to its own separate document?  
  
**@ 18:36:16 | From Dylan**  
although then the user manual will literally only say to use wasd to move  
  
**@ 18:41:51 | From Michael**  
Oh sorry, didn't see your message before. Version description is supposed to be a separate document, so we should probably split it off. The user manual does also have the goal of the game and stuff, so it at least has some stuff different from version description.  
  
Also, Confer said the version description is basically a description of everything you have by the end of the cycle, including any defects and such. He said it'll basically be a bullet-list, not so much full paragraphs.  
  
**@ 18:43:13 | From Dylan**  
are you and josh by chance gonna do the code reviews for sound, menus, and/or ui before wednesday? idk whether to put code reviews for those on the peer evals  
  
**@ 18:45:48 | From Michael**  
I'd imagine not, I doubt I'm going to have any free time before the presentation  
  
**@ 18:45:57 | From Dylan**  
k  
  
**@ 18:48:36 | From Michael**  
You gonna write the version description or do you want me to do it?  
  
**@ 18:52:04 | From Dylan**  
I'll do the version description  
  
**@ 18:52:12 | From Michael**  
Alright sounds good  
  
## March-05-2024  
**@ 19:40:00 | From Michael**  
@Josh Should've asked sooner, but what's the name of the Menu/Titlescreen feature? Some places we use one name and some we use another, and I want to make sure we're consistent so that there's no confusion when we submit the deliverables.  
  
**@ 19:41:15 | From Josh**  
We’ve used menu and title screen interchangeable  
  
**@ 19:41:20 | From Josh**  
I’m fine with either  
  
**@ 19:42:01 | From Michael**  
Alright, I I'll go with Menu since that's what's listed as the feature name in the weekly report  
**Reactions:** 👍  
  
**@ 20:02:23 | From Dylan**  
michael when you talk about the town in the presentation you should maybe mention the render group stuff since it isnt really obvious but will show design consideration  
  
**@ 20:02:39 | From Michael**  
Yeah that's a good idea, I'll do that  
  
**@ 20:21:31 | From Dylan**  
i did the version description lmk or change it if you have recommendations/issues  
  
**@ 20:22:02 | From Michael**  
Alright sounds good, I'll take a look at it in a bit  
  
**@ 21:18:47 | From Dylan**  
josh you wanna be the tester for loot? we havent had you be the tester for much  
  
**@ 21:19:05 | From Josh | Replying to Dylan: "josh you wanna be the tester for loot? w..."**  
Sure do :)  
  
## March-06-2024  
**@ 12:10:41 | From Josh**  
Reminder: don't say "I"  
**Reactions:** 👍  
  
## March-10-2024  
**@ 21:50:41 | From Dylan**  
i just realized we're still supposed to log this week under cycle 1 so im gonna undo how i set the this-cycle hours to 0 on the weekly report  
  
**@ 12:43:10 | From Dylan**  
oh i guess according to the new email we gotta put the new cycle intent for cycle 2 on this status report  
  
**@ 12:58:31 | From Dylan**  
also since it's been 2 weeks we kinda gotta remove the entity movement thing from risks  
  
**@ 12:58:38 | From Michael**  
Hmm okay, I just wrote out a new system and cycle 2 intent that we could use. Pretty much the same as what we already had, ofc  
  
Cycle 2  - To create an endless runner video game where the player collects loot and avoids simple enemies in a Wild-West style town.   
* Not sure if "simple" is good to include or not  
  
Sys  - To create an endless runner video game where the player collects loot and tools, avoids lighting bolts, and fights enemies, all in a Wild-West style town.   
* I Tried to add more specificity like "fights" enemies and collects "tools" to help differentiate it from the cycle intent  
  
**@ 12:58:41 | From Dylan**  
can we remove that since you did it as a feature?  
  
**@ 12:59:20 | From Dylan | Replying to Michael: "Hmm okay, I just wrote out a new system ..."**  
this is good although we should also say the player will be selectable in the system intent  
  
**@ 12:59:35 | From Dylan**  
also idk if "simple" is good to include for enemies  
  
**@ 13:00:08 | From Michael**  
Okay so probable just leave simple out, and yeah including the fact that they'll be multiple playable characters is a good idea  
  
**@ 13:00:40 | From Michael**  
Also I'll move that risk to obstacles since I've finished it (at least it seems finished)  
  
**@ 13:01:10 | From Dylan**  
k  
  
**@ 13:01:34 | From Dylan**  
maybe make another indented bullet under it and say you fixed it  
  
**@ 13:02:02 | From Michael**  
Alright will do  
  
**@ 13:04:19 | From Michael | Replying to Michael: "Hmm okay, I just wrote out a new system ..."**  
For the system intent, maybe "To create an endless runner video game with several playable characters, where the goal is to collect loot and tools, avoid lighting bolts, and fight enemies, all in a Wild-West style town. "  
  
Then the cycle intent would be the same but without the word "simple"  
  
**@ 13:04:52 | From Dylan**  
ok i will also say the town is endless  
  
**@ 13:05:05 | From Dylan**  
i also kinda want to mention that there will be a leaderboard in cycle 2  
  
**@ 13:06:18 | From Michael**  
Okay that sounds good, you mind writing that up then?  
  
**@ 13:06:56 | From Michael**  
Or do you want me to?  
  
**@ 13:07:59 | From Dylan**  
ACTION: Type = default  
  
**@ 13:08:32 | From Dylan**  
that good?  
  
**@ 13:09:59 | From Michael**  
Yup I think so  
  
**@ 13:10:10 | From Dylan**  
im not sure what to do for next week's goals  
  
**@ 13:10:23 | From Dylan**  
who wants to do the scoreboard/leaderboard?  
  
**@ 13:10:47 | From Dylan**  
that and the game over screen will probably be pretty similar and maybe not toooo hard  
  
**@ 13:11:03 | From Dylan**  
the enemy stuff will probably be more complicated and should probably have 2 programmers  
  
**@ 13:13:59 | From Michael**  
I can be one of the programmers for enemies  
  
**@ 13:14:04 | From Dylan**  
me too  
  
**@ 13:14:30 | From Michael**  
I guess for goals it would be to write up all documentation for Scoreboard, Enemies, and Loot (if it's not already finished)  
  
**@ 13:15:32 | From Dylan**  
you should probably be one of the programmers for the scoreboard or game over screen so that our number of programming and testing roles are balanced out  
  
**@ 13:15:40 | From Michael**  
Alright sounds good  
  
**@ 13:20:19 | From Dylan**  
ok i think my stuff is pretty much done. i might not be at the computer or be able to use my phone at 5 so if im not on just add my hours on there  
  
**@ 13:20:56 | From Michael**  
Alright, want me to submit it this week?  
  
**@ 13:21:47 | From Dylan**  
either you or josh once he adds his stuff  
  
**@ 13:21:56 | From Michael**  
Okay sounds good  
  
**@ 14:16:20 | From Michael**  
@Josh Make sure to add in any work you've done to the new status report. I think Dylan put you down for working on Loot Design Docs with him, but I think that's all that's in there for you at the moment.  
  
**@ 14:30:15 | From Josh | Replying to Michael: "<@544680424954134533> Make sure to add i..."**  
I didn’t have any time after the presentation to do work this week :( I will have plenty of time this week though!  
  
**@ 14:32:37 | From Michael | Replying to Josh: "I didn’t have any time after the present..."**  
Gotcha no worries, this week was kinda awkward anyways with it being between cycles and right before midterms / spring break, so I think confer would be fine with people taking it easy for a minute lol  
  
**@ 14:33:03 | From Michael**  
Just wanted to make sure that we don't miss anything for the report  
**Reactions:** 👍  
  
## March-11-2024  
**@ 18:08:52 | From Dylan**  
michael i made the basic enemies branch off of your new movement branch because  i think the more complex coordinates will help with enemy stuff like projectile angles  
  
**@ 18:48:26 | From Dylan**  
ACTION: Type = default  
  
**@ 18:49:20 | From Dylan**  
i did not design the bullets to look like that, it seems the pygame.transform rotation function actually does that with super low res images (before they're scaled up)  
  
## March-13-2024  
**@ 10:38:04 | From Michael**  
Sorry, I've been pretty busy over the past couple of days, but okay gotcha. That is kinda weird with the bullets but I guess it makes sense since we're not scaling anything up.  
  
## March-31-2024  
**@ 13:34:15 | From Dylan**  
Happy Easter!  
  
**@ 13:34:50 | From Dylan**  
Idk if I'm gonna be on the computer at 4 or 5 but my hours should be at the bottom and I think i listed all my weekly accomplishments and put some possible goals for next week  
  
**@ 14:01:48 | From Michael**  
Happy Easter! I can submit it if needed, although I might be a little late, maybe 5-6 ish. But same here, my hours are at the bottom and I added a couple other things to the report.  
  
**@ 14:03:07 | From Michael**  
@Josh Don't wanna make you do work on a holiday but just make sure your progress on the Game Over Screen is up-to-date in the report, then add your hours. After that I think we should be good to submit.  
  
**@ 14:53:46 | From Josh | Replying to Michael: "<@544680424954134533> Don't wanna make y..."**  
Ok give me a sec  
  
**@ 16:21:10 | From Dylan | Replying to Josh: "Ok give me a sec..."**  
I added me and michaels hours to the chart, your hours are all that are left to add and then it should be ok to submit after removing the list at the bottom  
  
**@ 16:51:03 | From Josh**  
I can add them in a couple minutes  - was w my family for Easter  
  
**@ 17:02:05 | From Dylan**  
i submitted an early copy just so we would have it in around 5, pls resubmit with your changes/hours after you can add them  
  
**@ 17:10:29 | From Josh | Replying to Dylan: "i submitted an early copy just so we wou..."**  
Thanks. Resubmitted  
  
**@ 17:10:47 | From Dylan**  
Ok have a good rest of your Easter  
  
## April-06-2024  
**@ 11:09:03 | From Michael**  
@everyone Since the presentation is this Wednesday, do you guys want to find a time to call and work on it? Maybe also do some code reviews / testing / merging if our code is finished? I'll be free anytime today or tomorrow, so most any time will work for me if you're up for it.  
  
**@ 11:14:06 | From Dylan**  
Yeah maybe sometime today I'll message when I'm at home  
  
**@ 11:34:37 | From Michael**  
Alright sounds good  
  
**@ 12:01:06 | From Josh | Replying to Michael: "@everyone Since the presentation is this..."**  
I don't have time today  - currently running a hackathon  
  
**@ 12:01:16 | From Josh**  
I should have time sunday  
  
**@ 12:08:14 | From Michael | Replying to Josh: "I should have time sunday..."**  
Gotcha gotcha, Sunday works for me. It would be best if all three of us could meet on Sunday, but if Dylan's busy tomorrow I could probably meet with him today and you tomorrow.  
  
**@ 12:13:07 | From Dylan**  
Idk about tomorrow but i could do the code review for scoreboard with Michael and Michael could do the code review for game over with Josh if we can't all meet  
  
**@ 12:22:42 | From Dylan**  
I could also review enemies w Michael and then you could review enemies with each other and that would be done  
  
**@ 12:30:46 | From Michael**  
That would work for me  
  
**@ 14:31:20 | From Dylan**  
@Michael ill be available in like 5 minutes  
  
**@ 14:33:50 | From Michael | Replying to Dylan: "<@616822981305434132> ill be available i..."**  
Sorry just something came up, I should be ready soon-ish though, 30 min at the latest  
  
**@ 14:37:36 | From Dylan**  
ok @ me  
  
**@ 14:48:02 | From Dylan**  
Josh i was just looking at the options menu quick and I think all the tests pass, but since there's no visual indication of any of the volume levels it's kinda hard to tell if your buttons are doing anythin/how much they are changing  
  
**@ 14:49:04 | From Dylan**  
In the design doc i think we should add something like either a bar to show the volume between a max and min value, or even just a value after the volume name like "- Music Volume: 75 +"  
  
**@ 14:49:20 | From Dylan**  
also i dont think there should be an 's' at the end of "Sound FXs"  
  
**@ 14:51:27 | From Michael**  
@Dylan  sorry about that, I'm in gen-dev-voice now  
  
## April-07-2024  
**@ 11:25:19 | From Dylan**  
@everyone if we are gonna meet today when are you available  
  
**@ 11:25:35 | From Dylan**  
I'm probably available most of the day but i might be busy for a couple hours at some point  
  
**@ 11:50:15 | From Michael**  
Any time works for me as well, I just won't be able to stay for terribly long since I'm a bit behind on homework  
  
**@ 13:20:46 | From Josh | Replying to Dylan: "@everyone if we are gonna meet today whe..."**  
Something came up today but I could meet tomorrow if you want  
  
**@ 13:23:21 | From Dylan**  
Idk maybe but i will be busy till like 5:30 or a little later probably  
  
**@ 13:24:54 | From Dylan**  
So are we deciding that we should do a player attack feature for cycle 3?  
  
**@ 13:33:12 | From Michael | Replying to Josh: "Something came up today but I could meet..."**  
I can probably meet sometime tomorrow night, but I can't say for certain  
  
**@ 13:33:30 | From Michael | Replying to Dylan: "So are we deciding that we should do a p..."**  
I feel like that would be a good idea  
  
**@ 13:33:51 | From Dylan**  
btw there's no assignment dropbox for the current status report so idk if we have to submit it  
  
**@ 13:34:03 | From Dylan**  
it's not like we would go over it in class this week  
  
**@ 13:34:15 | From Josh | Replying to Dylan: "btw there's no assignment dropbox for th..."**  
maybe not since we have an upcoming cycle ending? Or because we don't have class monday?  
  
**@ 13:35:05 | From Dylan**  
yeah we gotta make sure we print it to submit wednesday though  
**Reactions:** 👍  
  
**@ 13:35:37 | From Dylan**  
Also josh are you good with the player attacks feature?  
Who should be the programmers and tester?  
  
**@ 13:36:33 | From Dylan**  
i could be one of the programmers (or the only one if we only do 1)  
  
**@ 13:37:22 | From Josh**  
I can be the tester  
  
**@ 13:37:39 | From Dylan**  
ok michael you can be a programmer too if you want  
  
**@ 14:12:52 | From Michael | Replying to Dylan: "ok michael you can be a programmer too i..."**  
Sounds good to me  
  
**@ 16:44:35 | From Dylan**  
@everyone he posted a dropbox for the status report so we need to actually get it turned in. Michael and josh add your hours and accomplishments please  
  
**@ 17:03:38 | From Dylan**  
josh ik the scoreboard was really complex when we looked it over pls make sure you dont lowball all the work you did on that in terms of hours (not saying you are but just making sure bc i know it was pretty complex and took a lot of work)  
  
**@ 17:04:16 | From Josh | Replying to Dylan: "josh ik the scoreboard was really comple..."**  
I didn't make the scoreboard?  
  
**@ 17:04:16 | From Dylan**  
oops michael i mean lol  
**Reactions:** 👍  
  
**@ 17:05:23 | From Michael**  
Nah don't worry I'm not lowballing, I had it practically finished last week, this week was just making the text box and doing some minor cleaning up, so it wasn't too many hours  
  
**@ 17:06:07 | From Josh**  
I'm all set on the status report 👍  
  
**@ 17:07:11 | From Michael**  
Yup same here  
  
**@ 17:07:22 | From Dylan**  
michael you put yours in the chart you mean?  
  
**@ 17:07:37 | From Michael**  
Oh no, sorry I'll do that  
  
**@ 17:08:37 | From Michael**  
Okay done  
  
**@ 17:09:31 | From Michael**  
Also, anyone have any objections if I start merging stuff together tonight? It needs to happen before the presentation so I wanna try to get it done early  
  
**@ 17:09:39 | From Dylan**  
yeah thats fine  
  
**@ 17:10:31 | From Dylan**  
idk how scoreboard, options and game over all work internally but i already merged loot with enemies so the actual in-game stuff shouldnt conflict too much with your other stuff  
  
**@ 17:11:06 | From Dylan**  
aside from creating the player after you press start  
  
**@ 17:11:28 | From Michael**  
Gotcha gothca, that's good  
  
**@ 17:11:53 | From Dylan**  
I submitted the report  
  
**@ 17:12:10 | From Michael**  
Alright nice!  
  
## April-08-2024  
**@ 08:25:39 | From Dylan**  
Josh idk if you are gonna be doing any work on the project during the day today but if you are, maybe look at the test suites and testing on loot and enemies  
If we get the testing for those done then i think we can finish all the testing and code reviews by the end of tonight (assuming we meet tonight)  
  
**@ 10:06:12 | From Josh**  
Doing the testing was my plan today :)  
  
**@ 13:53:18 | From Josh**  
@Michael I fixed the game over music not looping  
  
**@ 17:42:08 | From Dylan**  
@everyone im online now, lmk if you can meet  
  
**@ 17:49:53 | From Michael | Replying to Josh: "<@616822981305434132> I fixed the game o..."**  
Gothca, I'll see if I can get that testing finished tonight  
  
**@ 17:50:38 | From Michael | Replying to Dylan: "@everyone im online now, lmk if you can ..."**  
I can meet, I just won't be able to for long, maybe 30-40 ish  
  
**@ 17:52:12 | From Dylan**  
ok is that like a total time limit for tonight bc youre busy or just bc you gotta do something in 30-40 min?  
If you are just busy ill wait till josh is available but if you might also be available later we can meet now  
  
**@ 17:53:21 | From Michael**  
Just a total time limit, I can meet most any time. I still gotta work on merging everything and I got a couple other assignments I need to start working on  
  
**@ 17:53:40 | From Dylan**  
ok ill wait till josh is also available  
  
**@ 17:53:45 | From Michael**  
Alright sounds good  
  
**@ 18:12:10 | From Josh**  
I'm free right now for a couple minutes if y'all need  
  
**@ 18:12:47 | From Dylan**  
I made another branch merging game over, options menu, and scoreboard. There might be some issues, i know the game over animation plays at the wrong size, but i wanted to get some of that done since youre busy michael  
  
**@ 18:12:58 | From Dylan**  
I would meet rn but i gotta eat ill be back in a little bit  
**Reactions:** 👍👍  
  
**@ 18:48:58 | From Dylan**  
@everyone  ok im on again  
  
**@ 18:55:53 | From Josh**  
I’m grabbing food  
  
**@ 19:12:10 | From Dylan | Replying to Dylan: "I made another branch merging game over,..."**  
that mentioned size error is fixed now  
**Reactions:** 👍  
  
**@ 19:27:12 | From Josh**  
I am back  
  
**@ 19:29:34 | From Michael**  
Alright I'm here too  
  
**@ 19:30:31 | From Dylan**  
ok join  
  
## April-13-2024  
**@ 16:55:17 | From Dylan**  
if we're gonna do an installable/executable/exe file *feature* i was thinking both of you 2 could be the programmers and i could be the tester since you both mentioned having done that or looked at it before  
  
**@ 16:55:50 | From Dylan**  
if youd rather not thats fine but i thought id mention it in case either of you were thinking abt it or were gonna start some work on it  
  
**@ 16:56:12 | From Josh**  
I can be the programmer for that  
  
## April-14-2024  
**@ 13:54:23 | From Dylan**  
We havent merged the cycle 2 branch into main yet have we? can I do that?  
  
**@ 13:55:16 | From Michael**  
Sure, that's good with me  
  
**@ 13:55:38 | From Michael**  
Oh and yeah I can be a programmer for the installable feature  
  
**@ 13:56:31 | From Michael**  
Or the "person B" for it  
  
**@ 13:58:15 | From Dylan**  
ok i merged cycle 2 into main and made a backup branch of the previous (cycle 1) main branch  
  
**@ 14:00:48 | From Dylan**  
also all my hours and achievements are on the status report. Since its a new cycle we gotta reset the hour numbers in that column. Ik last cycle we split the weeks hours between the 2 cycles but personally id prefer to just log them all under cycle 3 so its easier and we can just get those starting hours logged in the new cycle  
  
**@ 14:01:04 | From Dylan**  
but lmk if youre not ok with that  
  
**@ 14:17:15 | From Michael**  
Yeah that sounds good  
  
## April-15-2024  
**@ 18:45:14 | From Josh**  
@Dylan Just was doing some work for deployment and played the game. Just wondering if this is intentional (and I forget if we talked abt it today): if the player is hit, they get a cooldown from that specific enemy, but *not* from everything. So if 3 zombies hit the player at the same time, 60 damage is taken, 20 from each. Do we want invulnerablility from everything when hit or just the thing that hit us?  
  
**@ 18:47:30 | From Dylan**  
are you sure its not from everything? Also i just looked and noticed that the lightning striking uses the direct lower_health function, which bypasses iframes, so if youre testing with lightning it wasnt gonna work atm. I will change lightning to use damage() instead of lower_health() so it follows the iframe rules  
  
**@ 18:48:29 | From Josh**  
I'm currently testing on the main branch, but I can double check 👍  
  
**@ 18:48:59 | From Dylan**  
also the iframes are kinda short so it might be hard to notice anyways  
  
**@ 18:49:08 | From Josh | Replying to Dylan: "also the iframes are kinda short so it m..."**  
ohh that might be it  
  
**@ 18:49:12 | From Josh**  
how short are they?  
  
**@ 18:49:22 | From Dylan**  
the main reason i even did the iframe system was so projectiles wouldnt damage you 10 billion times before passing through you  
**Reactions:** 👍  
  
**@ 18:49:44 | From Dylan**  
i think it was 30 so half a second  
  
**@ 18:50:13 | From Josh**  
I gotcha! Well just wondering... do *we want* to have a longer invulnerability? I'm good with either but without it, you can die reallyyy quickly depending on the scenario  
  
**@ 18:50:40 | From Dylan**  
I can if you want  
  
**@ 18:51:00 | From Josh**  
Oh also good news, I'm pretty sure I got the installer working!  
  
**@ 18:51:47 | From Dylan**  
Also rn the players and enemies have the same iframes, i should separate them because i just set the enemy iframes really low bc the ninja throws every 15 frames, so I set the enemy iframes to only 15 so every projectile would actually hit. Meanwhile the player iframes might be better at like 60  
**Reactions:** 👍  
  
**@ 18:52:00 | From Dylan | Replying to Josh: "Oh also good news, I'm pretty sure I got..."**  
good job its good thats functional  
  
**@ 18:52:12 | From Josh | Replying to Dylan: "good job its good thats functional..."**  
so it's not just an exe for the game. The installer puts everything into C:\Program Files\LBT  
  
**@ 18:53:21 | From Dylan**  
can the user run easily without having to run it with python from a command line or in an IDE?  
  
**@ 18:53:28 | From Josh**  
yep!  
  
**@ 18:53:32 | From Josh**  
The installer is an exe file  
  
**@ 18:53:39 | From Josh**  
Run that, install like a normal app, run game  
  
**@ 18:53:56 | From Dylan | Replying to Josh: "The installer is an exe file..."**  
I mean the actual game after running the installer  
  
**@ 18:54:37 | From Josh | Replying to Dylan: "I mean the actual game after running the..."**  
yep, you can search for the game in the windows menu, or use the desktop shortcut it makes on the desktop  
  
**@ 18:54:58 | From Josh**  
Just need to make sure it runs on a windows laptop that doesnt have python already  
  
**@ 18:55:00 | From Josh**  
Pretty sure it will  
  
**@ 18:55:31 | From Dylan | Replying to Josh: "yep, you can search for the game in the ..."**  
Oh thats cool it shows up in the menu too  
  
**@ 18:59:15 | From Dylan | Replying to Josh: "<@554395967609241640> Just was doing som..."**  
ok i was really mistaken, i forgot to switch the zombies from lower_health() to damage() too, so they werent following iframes either, only their attack cooldowns  
  
**@ 19:01:09 | From Dylan**  
that stuff will still be weird on your branch but you can just switch to selectable player if you want to test since its basically just a newer version of player attacks at this point  
**Reactions:** 👍  
  
## April-16-2024  
**@ 20:32:45 | From Dylan**  
ok basically the selectable player feature is completely done  
  
**@ 20:34:17 | From Dylan**  
im just gonna do the deployment testing and stuff in class wednesday, josh can you look some more at the description since there are no constraints right now  
  
**@ 21:42:29 | From Dylan**  
Actually considering that, Michael when you do the customizable options feature you could just build off of the selectable player branch, that way there will be nothing at all to merge at the end of the cycle except applying the deployment stuff  
  
## April-17-2024  
**@ 07:59:37 | From Dylan**  
Confer says he's not gonna be in class today but we're still gonna meet right?  
  
**@ 08:57:10 | From Michael**  
I'm planning on meeting  
  
**@ 11:39:39 | From Dylan**  
I'm probably gonna be a bit late to class but I'll be there  
  
**@ 11:40:26 | From Josh**  
Isn’t class cancelled?  
  
**@ 11:40:48 | From Dylan**  
Confer won't be there but I still wanna go so we can get stuff done  
  
## April-22-2024  
**@ 17:18:08 | From Dylan**  
I just realized, for the presentation on Wednesday, whoever is doing the demo should bring a mouse if you have one. The player attacks are pretty hard to do on a laptop trackpad  
  
**@ 17:18:28 | From Michael**  
Alright gotcha, I can bring one  
  
**@ 18:06:37 | From Josh**  
I also have a spare usb mouse I can bring if needed  
  
## April-23-2024  
**@ 10:52:21 | From Dylan**  
Hope y'all are having a good morning, I just wanna make sure we have everything planned to be ready tomorrow. Michael are you gonna be able to print the necessary papers and put the final deliverable folder on a spare usb stick to bring tomorrow? Josh are you gonna have those 2 test suites/logs done today and put some stuff about them on the slideshow?  
  
**@ 11:01:40 | From Josh**  
Yep! I’ll also make sure everything is ready for the installer so I can demo it for him  
  
**@ 11:03:26 | From Dylan**  
Oh also make sure both of you do and print your peer evaluations. Mine is printed and in the binder already. Josh i am typing an early version of the installation guide rn bc i know youre busy with the testing  
  
**@ 11:03:52 | From Dylan**  
Also we need to merge the features, which should be easy with no conflicts but just remember we should probably do it  
  
**@ 11:08:20 | From Dylan**  
Here is the start menu screen i was talking about yesterday josh, there isnt a problem with it or anything but its just kinda weird it didnt show up for you  
  
**@ 11:09:40 | From Josh**  
Weird! But I mean… it probably works no matter where we put all the files as long as the exe is in the same dir as the assets and other files  
  
**@ 11:10:20 | From Dylan**  
Yeah it should work fine, im gonna add it as an installation step but say it may not appear on some systems or something  
  
**@ 11:25:39 | From Dylan**  
Ok so i messed with it some more and you have to use the "add and remove programs" windows settings menu thing to delete lightning bolt town, then when you run the installer again it will give you both full install menus. But i cant get the program to actually show up in the start menu no matter what i do  
  
**@ 12:35:56 | From Michael | Replying to Dylan: "Hope y'all are having a good morning, I ..."**  
Yup I can do that  
  
**@ 12:40:37 | From Dylan**  
@Josh how do you compile or whatever the installer/update it in regard to changes in the installer.iss file? I think i can make it work for the start menu but idk how to update the installer  
  
**@ 12:41:22 | From Dylan**  
ACTION: Type = default  
  
**@ 12:41:50 | From Josh**  
I can make instructions for that after lunch 🫡  There's a specific program on my pc that does it, I'm just blanking on the name.  
  
**@ 12:42:02 | From Josh**  
I can also do the updating for the installer, it's on my agenda for today  
  
**@ 12:42:13 | From Dylan**  
Ok try the stuff in those screenshots to see if it works for the start menu pls  
  
**@ 12:42:34 | From Dylan**  
I already made a draft of the installation guide, just go over it once you are totally finished with the installer  
  
**@ 12:42:40 | From Josh**  
What do you mean "make it work for the start menu"  
  
**@ 12:43:10 | From Dylan | Replying to Dylan: "Here is the start menu screen i was talk..."**  
I specify a desired start menu folder here but the program doesnt actually appear in the start menu  
  
**@ 12:43:27 | From Dylan | Replying to Dylan: "..."**  
but i think this would maybe fix it but idrk  
  
**@ 12:43:50 | From Dylan**  
and i dont want confer to see that it asks for one and then check the start menu but it isnt there  
  
**@ 12:43:57 | From Josh**  
🤷‍♂️ I can give it a try but my Windows 10 machine won't even ask me to specify a directory  
  
**@ 12:44:08 | From Dylan | Replying to Dylan: "Ok so i messed with it some more and you..."**  
try this  
  
**@ 12:44:08 | From Josh**  
so if we don't specify a directory... it works  
  
**@ 12:44:13 | From Josh**  
okay  
  
**@ 17:24:36 | From Dylan | Replying to Dylan: "..."**  
Ok so i ran the script to create the installer, and i also ran it after adding the line here. With that line added, the folder actually is created in the start menu, however it literally creates a folder called "(Default)" by default. Idk if there's a way to change that, otherwise we should probably specify for them to type in a new folder for lightning bolt town or something  
  

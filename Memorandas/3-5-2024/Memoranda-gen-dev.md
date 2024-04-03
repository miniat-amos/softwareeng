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
  

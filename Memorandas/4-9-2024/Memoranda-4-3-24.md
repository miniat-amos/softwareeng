# Channel: 4-3-24  
## April-03-2024  
**@ 10:44:49 | From Michael**  
Sorry yall, but I'm still feeling pretty rough so I won't be able to make it to class today either. Since I won't be there I'll add some notes here on the stuff I've worked on and will be working on:  
  
The scoreboard is practically complete, I'll just have to add the ability to filter by username. The only other thing missing is a place for the user to ender their username, but I'm not sure if that should be a part of Game Over or Scoreboard. Either way is fine with me. I'll add more info to the design docs to make sure it's clear how it works.  
  
I'll get to work on creating a test suite for Game Over and test it once it's ready. Also, since our presentation is a week away, we should probably work on getting everything complete and merged into main. Maybe try to be ready to merge before Monday? Or if we can get stuff finished and tested quick enough I can work on merging over the weekend or something.  
  
**@ 11:35:48 | From Dylan**  
Also we're not in class Monday  
  
**@ 11:36:35 | From Michael**  
Oh right, so we should definitely try to get things merged soon, and start working on the presentation.  
  
**@ 11:37:37 | From Josh**  
I'll also not be in class today. Got a sore throat. Don't really feel *sick* besdies that, but I'd rather just work async today. I'll be checking out the static version of the music manager and converting my current options menu code over to that!  
  
**@ 11:58:01 | From Dylan**  
Ok uh is it possible for any code reviews to be done virtually like this? Bc we won't be in class again before the presentation  
  
**@ 11:58:16 | From Dylan**  
I will probably merge enemies and loot during class time today  
  
**@ 11:59:41 | From Michael**  
I don't see why not, although we should probably hop on a call and screen share instead of just messaging  
  
**@ 12:09:45 | From Dylan**  
Also feel better soon both of u  
**Reactions:** ❤️  
  
**@ 12:14:12 | From Dylan**  
Meeting Summary  
Josh and Michael were out sick today  
Dylan worked on merging Loot and Enemies during class  
Worked on cycle 2 presentation/deliverables during class  
  
**@ 13:06:30 | From Dylan**  
I put/made folders indicating instructions for each deliverable in the cycle 2 deliverables folder on the google drive. The presentation is also there under administrative digest. I made rough versions of pretty much all the documents we need (version description, user manual, lessons learned, etc). We will still need to print stuff including our individual peer evaluations  
  
**@ 13:06:46 | From Dylan**  
But go thru those other things and check em over/add any of your stuff  
  
**@ 13:06:53 | From Dylan**  
also go through the presentation  
  
**@ 13:14:04 | From Michael**  
Sounds good, will do  
  
**@ 13:21:43 | From Dylan**  
Enemies and loot are merged in branch 29-enemies-loot-merge  
  
**@ 13:28:53 | From Dylan**  
We gotta remember that the user has to install sortedcontainers in order to run the game since scoreboard uses it  
  
**@ 13:29:39 | From Dylan**  
Michael i was gonna do testing on scoreboard but since it isn't integrated with game over it doesnt show after the player is killed, and when i press the main menu button the terminal asks for a "scoreboard code" idk what that is  
  
**@ 13:44:08 | From Dylan**  
Confer suggested the lightning should have the smoother movement with inertia like the zombies so i made them do that  
  

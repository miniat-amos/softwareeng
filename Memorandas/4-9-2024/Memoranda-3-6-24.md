# Channel: 3-6-24  
## March-06-2024  
**@ 12:14:11 | From Josh**  
Notes from the other presentations:  
- give a clear list of what features were implemented during the cycle  
-  
  
**@ 12:14:21 | From Dylan**  
- Mention design decisions in presentation  
- List features before demo  
  
**@ 12:15:01 | From Dylan**  
- List feature statuses (listed on feature overview, don't forget to mention)  
**Reactions:** 👍  
  
**@ 12:15:51 | From Dylan**  
- Lean into ending, don't be abrupt (should we move plans to last slides??)  
  
**@ 12:20:29 | From Josh**  
- have slides that can be read from the back of the class  
  
**@ 12:21:42 | From Michael**  
Not to be making too many last-minute changes, but should we move "Tools & Environment" and "Processes & Standards" to right before Features? I feel like that's a more natural place for it, rather than between Demo and Plans.  
  
**@ 12:21:57 | From Josh**  
good w me  
  
**@ 12:35:42 | From Josh**  
- make demos with colors that are easy to see  
  
**@ 12:35:52 | From Josh**  
***white against yellow is crazy***  
  
**@ 12:43:18 | From Michael**  
Credits might be good? Go full minecraft-mode and have it be a dramatic 10-minute narrative  
  
**@ 13:10:21 | From Josh | Replying to Michael: "Credits might be good? Go full minecraft..."**  
LOL  
  
**@ 13:10:30 | From Josh**  
play outro music when we finish  
  
**@ 13:21:44 | From Josh**  
***java*** 😭  
  
**@ 14:56:49 | From Michael**  
We didn't have time to really discuss any work today, and we should probably avoid making new features until we can discuss and work on them properly, so I made a list of some stuff we can work on. Only if you feel like you need to put some hours in, so no pressure. None of these are really feature on their own, just small additions or changes to existing code that have to make at some point.   
  
* Increase use of SETTINGS.py in some areas and add more settings if needed  
  * In particular, World and Building will likely need to use these settings more.   
  * There are probably other areas, so it might be work looking at your code and seeing if there's anything hardcoded that probably shouldn't be.   
* Work on resizable screen (see pygame.RESIZABLE)  
  * This will require adjusting the UI a bit to have it fetch screen size and calculate the size and position of components, rather than hardcoding them.   
  * Will probably also require some rework of Camera.   
* Create a screen for when the player dies (maybe with a score display and quit button)  
  
To keep myself busy, I'm going to work on getting entities to move by sub-pixels, i.e. storing position as a float, incrementing pos by floats, but squashing down to an int-based rect before collisions or rendering. Might pick something else too if that ends up being really quick. Midterms are comings so definitely no pressure, just putting some ideas out there so we don't idle too much.  
  
**@ 17:33:09 | From Dylan**  
oh i had done some stuff on the design doc for loot and made a loot class with key press spawning just to get that started  
  
**@ 17:33:58 | From Dylan**  
didnt mean to do that too ahead of time but i dont think it really conflicts with possible design decisions too much  
  
**@ 17:35:11 | From Michael**  
Nah you're all good, we need to start making at least some features so that's all good, I was more trying to say we shouldn't start making a bunch without talking about it first. Sorry, probably could've phrased it better.  
  
**@ 17:35:21 | From Dylan**  
no youre fine dw  
  

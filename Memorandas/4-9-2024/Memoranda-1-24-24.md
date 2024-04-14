# Channel: 1-24-24  
## January-24-2024  
**@ 12:41:45 | From Josh**  
**IDEs**  
- debugging  
- lang support  
- do not become dependent on autocomplete  
- utilize the tools that are out there  
- integrated Git support (avoid at all costs!) learn git from the command line  
  
**Testing**  
- Automate old testing to ensure things don't break upon new changes and save time  
  
**Large language model**  
- Can be helpful, but don't have them write large swaths of code  
- Google Bard is better in terms of generative ai   
  
**Arch spike**  
- Make a written plan for the spike  
- What are all the things we need to make / do / test  
- Mostly not great work across the board  
- The team needs to not have any abstraction of any part of the project  
- Decide who is responsible for which work  
- Get used to knowing how to debug your work  
- Don't be a "hero"  
- Don't "architect" too much / don't go far  
- All of this code is going to be thrown away after the spike to never be seen again!!!  
  
**The Minimally Viable Product Process** (MVPP)  
- When making a product or service, put together the dinkiest possible thing that can give you a return on investment  
- An agile XP variant: focus on quality delivered via software and demonstrated by minimally viable documentation  
  
**Quality Guarantors**  
- We cannot guarantee quality or if it will even ever finish running  
- We give the "sensation" of quality  
- We need to convince ourselves the product is good  
- Coding standards, and configuration management, software processes for software engineering  
  
**eXtreme Programming (XP)**  
- XP is an "agile" process: focus is on quality delivered via software products rather than through documentation  
- customer describes "stories" -> team costs stories -> customer select stories -> team develops stories  
  
  
**Agenda for today's class**:  
- Show how the camera works/go over new changes we made since Monday  
- Flesh out our plan for making the game (and assign people to that work)  
- Start working through some of that work  
  
**@ 13:37:46 | From Josh**  
**Process Drivers**  
  
System Intent  
- Mission statement and focus of the team   
- Described by Customer  - Written by team  
  
User features   
- Things to be implemented within the product  
- Described by Customer/Team, Selected by Customer, Cost by team, implemented by team  
- Needs a name, feature, and constraints   
- Keep details high-level   
  
Cycle intent  
- Lays out what you believe the product will be at the end of this cycle  
  
Pair Programming  
- Driver: person on the computer writing the code  
- Observer: watching and helping  
- Effects: mistakes caught as typed, "dont let me down" pressure, two heads better & faster than one, more enjoyable experience, tend to produce shorter programs  
  
Collaborative Adversarial Pairs  
- make the design docs together  
- the coder should never look at the tests that are made by someone else  
- pros: pair relaying, pair pressure, pair learning, satisfaction, design quality, minor co-location requirements, more efficient depending on feature size  
- cons: no continuous review  
  
**@ 13:50:22 | From Josh**  
**Things that need to happen next!**  
  
- Collision (so two *solid* objects collide and both stop moving) so a player hits a "wall" object and cannot move past it   
- integrating an animation with the Player class  
- adding lightning behavior  
- UI to show off health, healthbar, loot, experience  
  

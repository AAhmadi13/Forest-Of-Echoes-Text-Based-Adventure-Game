# Forest-Of-Echoes-Text-Based-Adventure-Game
# Python Text-Based Adventure Game


**FEATURES OF FOREST OF ECHOES V4:**

1. Added a storage system & using the item function in the inventory -                                                                                     ✅ **[STEVE]**
2. Added an examining items function for information or clues -                                                                                            ✅ **[STEVE]**
3. Added an access help function for available commands -                                                                                                  ✅ **[STEVE]**
4. Added a save game feature allowing you to continue a previous game from the last time it was saved -                                                    ✅ **[STEVE]**
5. Added an introduction at the start of the game to make it more understandable and to provide context for the user -                                     ✅ **[ADAM]**
6. Added 'help/ controls' command at the start of the game menu so that users don't get confused with controls early in the game -                         ✅ **[ADAM]**
7. Added an ending to the game with multiple endings, with unique endings based upon the user's choices with given prompts -                               ✅ **[ADAM]**
8. Added an ASCII map feature within the game -                                                                                                            ✅ **[ADAM]**
9. Expanded the examination function to allow users to have a wider range of choices with items -                                                          ✅ **[ADAM]**
10. Fixed/ changed the 'deep_cave' room so that the overall story flows more easily -                                                                      ✅ **[ADAM]**
11. Fixed/ changed overall story script so it's not repetitive and is consistent -                                                                         ✅ **[ADAM]**
12. Fix the map function so that the map text/ symbols are consistent & structured properly -                                                              ✅ **[STEVE]**
13. When you are in the final fight/ battle, it should prompt the user to absorb the 'heart of yurei' before getting into the battle, so the story makes more sense. **(recommendation: Put the sword in use so if the user does not choose or take the 'heart of yurei', it holds a consequence of losing the traveller due to the lack of power, which you would not suffer if the user chooses to take and absorb 'heart of yurei'.)** -                                                                   ✅ **[STEVE]**
14. Add back on the "examine" command on its own, to prompt the room description when needed -                                                             ✅ **[STEVE]**
15. Adapt the Finals Boss Room so that it is not hardcoded as a function (declarative style) -                                                             ✅ **[STEVE]**
16. Add two more 2 more rooms plus obstacles -                                                                                                             ✅ **[STEVE]**
17. Adapt the 'heart of yurei' to not be hard-coded (declarative style) -                                                                                  ✅ **[STEVE]**
18. Improve Show_map() to be more declarative style -                                                                                                      ✅ **[STEVE]**
19. When you absorb the heart of Yurei in the deep cave room, after you wake up, the game could prompt you to take a direction -                           ✅ **[ADAM]**
20. Fixed it so the Map is consistent within placement (swapped the location of the echoing ledge & whispering cave in the map) - ✅ **[STEVE]**
21. Fixed it so the map includes a 'you are here' arrow so players know exactly which room they are in - ✅ **[STEVE]**
22. Fixed the dialogue so that the relic isn't mentioned again if the player has taken it already - ✅ **[ADAM]**
23. Fixed the dialogue so that the traveller isn't mentioned again if the player has already freed the traveller - ✅ **[ADAM]**
24. Fixed it so if the player has taken the 'heart of yurei' and visited the 'deep cave' again, it will show a different dialogue, so it shows that the heart has been taken - ✅ **[ADAM]**
25. Fixed it so that if the player has opened the locked gate already within the 'glowing cave' and revisits the room, it will show a different dialogue so that it shows the gate is open - ✅ **[ADAM]**
26. Fixed it so that at the end of the game, it allows users to play again with a prompt - ✅ **[ADAM]**

[Latest]
28: Fix: command: take heart of yurei - This does not work | command: take heart_of_yurei - This does work ✅ **[STEVE]**
      use
      take
      examine
      
29: Fix: Logic for rescuing the traveller does not work ✅ **[STEVE]**

30: Improve: script at the end of achieving the enchanted sword ✅ **[STEVE]**

31: Fix: when using the inventory command, avoid prompting the room description, it happens with almost all commands, such as 'map' ✅ **[STEVE]**

32: Fix: save and load ✅ **[STEVE]**

33: Adapt: changes made from adam on past code to new ✅ **[STEVE]**

34: Fix: items should no longer prompt as in being present in the room if they are taken, this goes for all rooms Changing prompts to keep the sense of the context valid, e.g., if the relic is taken from the traveler, then no longer say the relic is on the traveller's hand  ✅ **[STEVE]**

35: respawn command works only in the maze ✅ **[STEVE]**

36: Dynamic prompting of room descriptions so that it makes sense after performing changes to it, such as rescuing the traveller, it should not longer prompt that the traveller is bonded to the vines when returned to the shrouded path room, the same goes for all other rooms ✅ **[STEVE]**

37: Fix: after loading game from a save file, the gate resets and you need to use the relic again, e.g., deep cave to glowing cave, then go deep cave again, and the gate is closed ✅ **[STEVE]**

38: Fix: Final boss battle death ending. As you are respawned back to the echoing ledge room after dying and enter the boss room again, the mountain peak introduction no longer prompts ✅ **[STEVE]**

39: Fix: Run sequence wasn't working ✅ **[STEVE]**

40: Save and load massive bug with obstacles being bypassed without needing the required items or helper ✅ **[STEVE]**

39: MUD Multi-User Dungeon - Plan and implement the game from being a single-player text adventure into a multi-player Multi-user dungeon (“MUD”) – this would mean that the game would benefit from being designed “from the ground-up” as capable of networking - ❌




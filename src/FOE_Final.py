import json
import os
from typing import Dict, List, Union, Callable, Any

# ========== AUTHORS: Adam H. Ahmadi 23160330 - Steve M. Aguilar 23166613 ==========

GAME_CONFIG = {
    "intro_text": """
The Forest of Echoes whispers your name, Alex.

You've come alone, driven by the legend of the Crown of Pyros — a treasure said to hold the power to bend fate itself.  
Your path leads to the summit of Mount Duskveil, where the treasure waits beyond shadows and ancient trials.

Every step you take echoes with danger and secrets long forgotten.

Trust no one, rely on your wits, and prepare to face the unknown.

Your journey begins now.
""",

    "boss_battle_outcomes": {
        "fight_sequence": {
            "no_heart": {
                "cover_choices": {
                    "prompt": "Pyros roars and unleashes a stream of fire! Where do you take cover?\n1. Wooden box\n2. Rubble pile\n3. Rock wall",
                    "options": {
                        "1": {
                            "lines": [
                                "\nThe wooden box bursts into flames instantly. You are engulfed and perish.",
                                "\n💀 THE END – Burned Alive 💀"
                            ],
                            "effects": {"fatal": True}
                        },
                        "2": {
                            "lines": [
                                "\nYou dive behind rubble, but suffer severe burns on your right hand.",
                                "Your right hand is injured and weak. You won't be able to wield your sword as effectively."
                            ],
                            "effects": {"set_flag": "right_hand_injured"}
                        },
                        "3": {
                            "lines": [
                                "\nYou take shelter behind a solid rock wall, shielded from the fire."
                            ]
                        }
                    }
                },
                "counter_choices": {
                    "prompt": "Pyros, enraged by your escape, charges toward you!\n1. Dodge\n2. Strike with your sword",
                    "options": {
                        "1": {
                            "lines": [
                                "\nYou quickly dodge to the side, narrowly avoiding Pyros' charge.",
                                "The dragon takes to the sky and begins circling above."
                            ]
                        },
                        "2": {
                            "lines": [
                                "\nYou swing your sword at the charging dragon!",
                                "It's a direct hit, but the recoil throws you backward as Pyros takes to the sky."
                            ]
                        }
                    }
                },
                "final_choices": {
                    "prompt": "The dragon circles above. Choose your final move:\n1. Time your strike and leap with your sword\n2. Run to the crown and escape\n3. Signal the traveler to help distract Pyros",
                    "options": {
                        "1": {
                            "lines": [
                                "\nYou leap with your sword, plunging it into Pyros as he dives.",
                                "The beast crashes into the mountain, but not before impaling you in flame.",
                                "The traveler catches your body as the world darkens.",
                                "\n💀 THE END – A Hero's Sacrifice 💀"
                            ],
                            "effects": {"fatal": True}
                        },
                        "2": {
                            "lines": [
                                "\nYou sprint to the Crown of Pyros and grab it as you flee.",
                                "The dragon crashes into the summit behind you, crushing the traveler in a blaze.",
                                "You have the crown, but at the cost of everything else.",
                                "\n🏅 THE END – Crown Without Power 🏅"
                            ],
                            "effects": {"concludes": True}
                        },
                        "3": {
                            "lines": [
                                "\nYou signal to the traveler. He nods and rushes to the side, hurling rocks and shouting.",
                                "Pyros turns his attention momentarily. You seize the opening and charge forward!",
                                "With a perfectly timed leap, you plunge the enchanted sword deep into the dragon's heart.",
                                "It thrashes, roaring in pain... and collapses.",
                                "Smoke rises. You and the traveler fall to your knees, exhausted but alive.",
                                "You and the traveler claim the legendary Crown of Pyros.",
                                "\n🏆 THE END – Dragon Slayer 🏆"
                            ],
                            "effects": {"concludes": True}
                        }
                    }
                }
            },
            "absorbed_heart": {
                "cover_choices": {
                    "prompt": "Pyros roars and unleashes a stream of fire! Where do you take cover?\n1. Stand your ground\n2. Conjure a barrier\n3. Dash behind enchanted rocks",
                    "options": {
                        "1": {
                            "lines": [
                                "\nSuddenly, you feel a surge of energy! The Heart's power courses through you.",
                                "Your burned arm begins to heal rapidly, and you feel lightning coursing through your veins.",
                                "You stand firm as the flames approach. The heart within you pulses brightly, shielding you in a fiery aura.",
                                "You are unharmed. Pyros growls in confusion."
                            ]
                        },
                        "2": {
                            "lines": [
                                "\nYou conjure a barrier using the heart's energy. The flames part around you.",
                                "The traveler watches in awe as your eyes glow crimson."
                            ]
                        },
                        "3": {
                            "lines": [
                                "\nYou and the traveler dive behind glowing rocks. The flames strike, but the rocks hold firm.",
                                "\nYou feel the Heart's power surging through you, lightning coursing through your veins.",
                                "You raise your hand and unleash a powerful lightning blast at Pyros!",
                                "The dragon roars in pain as the lightning strikes its scales."
                            ]
                        }
                    }
                },
                "counter_choices": {
                    "prompt": "Pyros charges toward you! The heart pulses with power.\n1. Blast Pyros with energy\n2. Dodge and empower your blade",
                    "options": {
                        "1": {
                            "lines": [
                                "\nYou release a burst of raw energy from your palm, striking Pyros mid-charge.",
                                "He reels back, scales charred, as he takes to the skies."
                            ]
                        },
                        "2": {
                            "lines": [
                                "\nYou dodge and channel the heart's power into your sword. It glows with ghostly fire.",
                                "You are ready for the final blow."
                            ]
                        }
                    }
                },
                "final_choices": {
                    "prompt": "Pyros circles above, wounded. Your heart burns with power.\n1. Challenge him head-on\n2. Force him down with magic",
                    "options": {
                        "1": {
                            "lines": [
                                "\nYou leap into the sky, sword blazing, and strike Pyros directly.",
                                "He crashes to the ground. You land beside him, unscathed.",
                                "The traveler steps forward, shielding his eyes from your glow.",
                                "\n👑 THE END – Ascension of the Flamebearer 👑"
                            ],
                            "effects": {"concludes": True}
                        },
                        "2": {
                            "lines": [
                                "\nYou summon chains of spirit flame that yank Pyros from the sky.",
                                "He lands with a thunderous crash, subdued and broken.",
                                "The traveler gasps. 'What... what are you becoming?'",
                                "\n👻 THE END – Master of the Heart 👻"
                            ],
                            "effects": {"concludes": True}
                        }
                    }
                }
            }
        },
        "run_sequence": {
            "prompt": "You flee the battlefield. The traveler runs with you but suddenly stumbles and falls behind.\nDo you go back to help or keep running?\n1. Help the traveler\n2. Keep running",
            "options": {
                "1": {
                    "lines": [
                        "\nYou run back and lift the traveler just as Pyros' flame scorches the trees.",
                        "Together, you duck behind a ridge. The traveler looks at you, grateful but wounded.",
                        "He hands you a dagger and nods. 'Let's end this.'",
                        "\nYou both return to face Pyros, scarred but determined.",
                        "(Continue to the battle sequence.)"
                    ],
                    "effects": {
                        "set_flag": "helped_traveler",
                        "continue_to": "cover_choices" #This will trigger the fight sequence
                    }
                },
                "2": {
                    "lines": [
                        "\nYou leave the traveler behind. You find refuge in a forest and a witch's hut.",
                        "Inside, a cup of water sits on the table. Do you drink it?"
                    ],
                    "next": {
                        "prompt": "Do you want to drink the water? (yes/no): ",
                        "options": {
                            "yes": {
                                "lines": [
                                    "\nYou drink the water, feeling a strange sensation. Your vision begins to blur...",
                                    "💀 THE END – Poisoned by the Witch 💀"
                                ],
                                "effects": {"fatal": True}
                            },
                            "no": {
                                "lines": [
                                    "\nYou decide not to drink the water. Exhausted, you lie down on the witch's bed and fall asleep.",
                                    "You wake up tied to a chair, the witch standing over you with a wicked smile.",
                                    "💀 THE END – Caught by the Witch 💀"
                                ],
                                "effects": {"fatal": True}
                            }
                        }
                    }
                }
            }
        },
        "hide_sequence": {
            "prompt": "You climb a tree to hide. A snake approaches you. What do you do?\n1. Kick the snake\n2. Jump down",
            "options": {
                "1": {
                    "lines": [
                        "\nYou try to kick the snake, but miss!",
                        "It bites you, injecting deadly venom.",
                        "\n💀 THE END – Snake Venom 💀"
                    ],
                    "effects": {"fatal": True}
                },
                "2": {
                    "lines": [
                        "\nYou jump from the tree, landing awkwardly on a hidden trap.",
                        "Spikes impale your legs.",
                        "\n💀 THE END – Impaled 💀"
                    ],
                    "effects": {"fatal": True}
                }
            }
        }
    },

    "rooms": {
        "forest_entry": {
            "description": "You stand at the edge of the Forest of Echoes. Mist clings to the ground. Paths stretch left and right.",
            "exits": {"left": "glowing_cave", "right": "shrouded_path"},
            "items": []
        },
        "glowing_cave": {
            "description": lambda state: (
                "Blue crystals pulse in the cave walls. A sealed gate blocks your path forward.\nThe gate's surface has indented markings - the shape suggests something\nsmall and angular should be placed there, though you see no keyhole."
                if not state["event_flags"].get("unlocked_gate", False)
                else "Blue crystals pulse in the cave walls. The gate stands open, revealing a path forward."
            ),
            "exits": {"right": "forest_entry"},
            "obstacle": {
                "name": "gate",
                "required_item": "relic",
                "success_msg": "The relic glows and unlocks the gate. The path forward is now open.",
                "effects": {
                    "set_flag": {"unlocked_gate": True},
                    "unlock_exit": "forward",
                    "unlock_destination": "deep_cave"
                }
            }
        },
        "shrouded_path": {
            "description": lambda state: (
                "A wounded traveler lies unconscious against a twisted tree, entangled in thick, living vines.\n"
                "A faint glint catches your eye — a relic lies near his hand, likely dropped before he collapsed.\n"
                "The vines look tough... you'll need something sharp to cut him free."
                if "relic" not in state.get("collected_items", []) and not state["event_flags"].get("helped_traveler", False)
                else "A wounded traveler lies unconscious against a twisted tree, entangled in thick, living vines.\n"
                     "The vines look tough... you'll need something sharp to cut him free."
                if not state["event_flags"].get("helped_traveler", False)
                else "The traveler stands free, rubbing his wrists where the vines once bound him. He nods at you gratefully."
            ),
            "exits": {"left": "forest_entry"},
            "items": lambda state: ["relic"] if "relic" not in state.get("collected_items", []) else [],
            "obstacle": {
                "name": "vines",
                "required_item": "enchanted_sword",
                "success_msg": "You slash the vines with your sword.\nThe traveler gasps in relief and thanks you. He now joins you as a companion.",
                "effects": {
                    "trigger_event": "free_traveler"
                }
            },
            "event": "traveler"
        },
        "deep_cave": {
            "description": lambda state: (
                "The Heart of Yurei floats above a stone altar, pulsing with silent energy, beckoning you to take it."
                if "heart_of_yurei" not in state.get("collected_items", [])
                else "The stone altar stands empty, with only faint traces of energy remaining."
            ),
            "exits": {"behind": "glowing_cave", "left": "whispering_cave", "right": "echoing_ledge"},
            "items": lambda state: ["heart_of_yurei"] if "heart_of_yurei" not in state.get("collected_items", []) else []
        },
        "whispering_cave": {
            "description":
                "The air is dense, and the echo of dripping water mixes with distant whispers.\n"
                "Ahead lies the entrance to a winding stone maze (go forward to enter).\n"
                "The ancients must have left clues to navigate it.",
            "exits": {"right": "deep_cave"},
            "items": lambda state: [] if state.get("maze_completed", False) or "enchanted_sword" in state.get("collected_items", []) else ["enchanted_sword"],
            "obstacle": {
                "name": "maze_entry",
                "direction": "forward",
                "success_msg":
                    "You step cautiously into the twisting maze ahead, the stone walls closing in around you.\nYou move forward through the winding passage... You see passages to your left, right and behind."
                    "\n*if you get lost, type 'respawn' to return out of the maze*"
            },
            "movement_handler": "maze",
            "maze": {
                "layout": [
                    ['#', '#', '#', '#', '#', 'S', '#', '#', '#', '#', '#', '#'],
                    ['#', ' ', 'T', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
                    ['#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
                    ['#', ' ', '#', 'T', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
                    ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
                    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
                    ['#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#'],
                    ['#', 'T', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
                    ['#', 'T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', '#'],
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
                ],
                "start": [1, 5],
                "exit_symbol": "E",
                "trap_symbol": "T"
            },
            "maze_completed": False,
            "reward_item": "enchanted_sword"
        },
        "echoing_ledge": {
            "description": lambda state: (
                "This narrow chamber hums with energy.\nIn front of you, a dusty stone pedestal holds a rolled-up parchment — its surface faintly glowing.\n"
                "To your right, a steep rock face rises high — too far to climb alone.\n(go 'right' to try climb the ledge)"
                if "maze_map" not in state.get("collected_items", [])
                else "This narrow chamber hums with energy. The stone pedestal stands empty.\n"
                     "To your right, a steep rock face rises high — too far to climb alone.\n(go 'right' to try climb the ledge)"
            ),
            "exits": {"left": "deep_cave"},
            "items": lambda state: ["maze_map"] if "maze_map" not in state.get("collected_items", []) else [],
            "obstacle": {
                "name": "high_ledge",
                "direction": "right",
                "description": lambda state: (
                    "The sheer cliff face towers above you. It's impossible to climb alone."
                    if not state["event_flags"].get("helped_traveler", False)
                    else "The traveler eyes the cliff and nods. 'Together we can scale this.'"
                ),
                "required_helper": "helped_traveler",
                "success_msg":
                    "With the traveler's help, you scale the high ledge to the mountain peak.",
                "effects": {
                    "unlock_exit": "right",
                    "unlock_destination": "mountain_peak",
                    "move_player": True
                }
            },
        },
        "mountain_peak": {
            "exits": {},
            "trigger_boss": {
                "prompt": "You stand atop the scorched summit of Mount Duskveil.\n"
                "Before you looms the colossal Fire Dragon, Pyros, its scales glowing like molten lava.\n"
                "The legendary Crown of Pyros rests upon a rock altar behind the beast, radiating power.\n"
                "This is the final confrontation. Your choices now will shape your fate.\n"
                "🔥 FINAL BATTLE - The Fire Dragon Pyros awakens! 🔥\nThe ground trembles. Smoke rises. You must decide:"
            }
        }
    },

    "items": {
        "relic": {
            "description": "An ancient relic pulsing with a soft, ethereal light. It seems to react to nearby energy."
        },
        "crown_of_pyros": {
            "description": "The mythical Crown of Pyros, forged from dragonfire and set with eternal rubies. It symbolizes triumph over the beast."
        },
        "heart_of_yurei": {
            "description": "A glowing, pulsating heart-shaped crystal. It hums with latent power waiting to be awakened.",
            "upon_take": "The Heart of Yurei pulses warmly in your hand, filling you with strange energy.\nAs you hold the Heart, you feel a strange connection to it. You should examine it more closely.",
            "interaction": {
                "prompt": "Do you want to absorb it or put it away? (absorb/put away): ",
                "options": {
                    "absorb": {
                        "lines": [
                            "As you hold the Heart close to your chest, it begins to glow intensely.",
                            "The crystal-like surface starts to shimmer and dissolve into pure energy.",
                            "You feel a warm sensation as the Heart fuses with your body, entering your chest.",
                            "A wave of energy courses through your veins, and your vision begins to blur...",
                            "[6 hours later]",
                            "You slowly regain consciousness, your body tingling with newfound energy.",
                            "A warm, electrifying sensation courses through your body, as if lightning flows in your blood.",
                            "The Heart of Yurei has become one with you, its power now a part of your very being."
                        ],
                        "effects": {
                            "set_flag": "absorbed_heart",
                            "remove_item": "heart_of_yurei"
                        }
                    },
                    "put away": {
                        "lines": [
                            "You carefully place the Heart in your bag, feeling its gentle pulse against your side."
                        ]
                    }
                }
            }
        },
        "maze_map": {
            "description": "A faded parchment showing the maze layout.\nKey turns are marked in red pigment — a clear guide through the Whispering Maze.",
            "interaction": {
                "prompt": "You unfold the parchment and study the sketch:",
                "display": """
+---+---+---+---+---+---+---+---+---+---+---+---+
| # | # | # | # | # | # | # | # | # | # | # | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # | T |   |   |   |   |   |   |   |   | E | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # | # | # | # |   | # | # | # |   | # |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # | T |   |   |   | # |   |   |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # | # | # |   | # | # |   | # | # | # |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # |   |   |   |   |   |   | # |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # |   | # | # |   | # | # | # |   | # |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # |   | # | T |   | # |   |   |   | # |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # |   | # | # |   | # |   | # |   | # |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # |   | T | # |   | S |   | # |   |   |   | # |
+---+---+---+---+---+---+---+---+---+---+---+---+
| # | # | # | # | # | ↓ | # | # | # | # | # | # |
+---+---+---+---+---+---+---+---+---+---+---+---+

S = Start, ↓ = Retreat (Return to Cave), T = Trap, E = Exit, # = Wall
"""
            }
        },
        "enchanted_sword": {
            "description": "A blade shimmering with arcane energy. It feels light yet deadly in your hands."
        }
    },

    "commands": {
        "help": {
            "description": "Show available commands",
            "action": lambda state: {
                "output": """
Commands:
- left/right/forward/behind: Move in a direction 
- examine: Examine area 
- examine [item]: Examine an item in your inventory
- take [item]: Pick up an item
- inventory: View your items
- use [item]: Use an item in the current location
- save: Save the game
- load: Load saved game
- map: View an ASCII map
- help: Show this help message
- quit: Exit the game
"""
            }
        },
        "go": {
            "description": "Move in a direction",
            "action": lambda state, direction, current_config: handle_movement(state, direction, current_config)
        },
        "examine": {
            "description": "Examine an item or the room",
            "action": lambda state, item=None: handle_examine(state, item)
        },
        "take": {
            "description": "Pick up an item",
            "action": lambda state, item, current_config: handle_take_item(state, item, current_config)
        },
        "use": {
            "description": "Use an item",
            "action": lambda state, item, current_config: handle_use_item(state, item, current_config)
        },
        "inventory": {
            "description": "View your inventory",
            "action": lambda state: {
                "output": "You have:\n" + "\n".join(f"- {item.replace('_', ' ')}"
                                                    for item in state["inventory"]) if state[
                    "inventory"] else "You have no items."
            }
        },
        "map": {
            "description": "Show map of current location",
            "action": lambda state: {"output": render_map(state["location"])}
        },
        "respawn": {
                "description": "Return to maze entrance (only works in maze)",
                "action": lambda state: handle_respawn(state)
            },
        "save": {
            "description": "Save the game",
            "action": lambda state: save_game(state)
        },
        "load": {
            "description": "Load the game",
            "action": lambda state: load_game(state)
        }
    },
    "obstacle_resets": {
        "glowing_cave": {
        "description": lambda state: (
            "Blue crystals pulse in the cave walls. A sealed gate blocks your path forward.\n"
            "The gate's surface has indented markings - the shape suggests something\n"
            "small and angular should be placed there, though you see no keyhole."
            if not state["event_flags"].get("unlocked_gate", False)
            else "Blue crystals pulse in the cave walls. The gate stands open, revealing a path forward."
        ),
        "exits": {"right": "forest_entry"},
        "items": [],
        "obstacle": {
            "name": "gate",
            "required_item": "relic",
            "success_msg": "The relic glows and unlocks the gate. The path forward is now open.",
            "effects": {
                "set_flag": {"unlocked_gate": True},
                "unlock_exit": "forward",
                "unlock_destination": "deep_cave"
            }
        }
    },
    "echoing_ledge": {
        "description": lambda state: (
            "This narrow chamber hums with energy.\n"
            "In front of you, a dusty stone pedestal holds a rolled-up parchment — its surface faintly glowing.\n"
            "To your right, a steep rock face rises high — too far to climb alone.\n"
            "(go 'right' to try climb the ledge)"
            if "maze_map" not in state.get("collected_items", [])
            else "This narrow chamber hums with energy. The stone pedestal stands empty.\n"
                 "To your right, a steep rock face rises high — too far to climb alone.\n"
                 "(go 'right' to try climb the ledge)"
        ),
        "exits": {"left": "deep_cave"},
        "items": lambda state: ["maze_map"] if "maze_map" not in state.get("collected_items", []) else [],
        "obstacle": {
            "name": "high_ledge",
            "direction": "right",
            "description": lambda state: (
                "The sheer cliff face towers above you. It's impossible to climb alone."
                if not state["event_flags"].get("helped_traveler", False)
                else "The traveler eyes the cliff and nods. 'Together we can scale this.'"
            ),
            "required_helper": "helped_traveler",
            "success_msg": "With the traveler's help, you scale the high ledge to the mountain peak.",
            "effects": {
                "unlock_exit": "right",
                "unlock_destination": "mountain_peak",
                "move_player": True
            }
        }
    }
    },
    "initial_state": {
        "location": "forest_entry",
        "inventory": [],
        "visited": ["forest_entry"],
        "event_flags": {
            "helped_traveler": False,
            "absorbed_heart": False,
            "right_hand_injured": False,
            "unlocked_gate": False,
            "unlocked_vines": False
        },
        "collected_items": [],
        "completed_obstacles": [],
        "maze_mode": False,
        "maze_position": None,
        "just_entered": True,
        "continue_battle_from": None
    }
}

SAVE_FILE = "savegame.json"

# ========== GAME LOGIC FUNCTIONS ==========

def apply_effects(state: Dict, effects: Dict) -> Dict:
    """Apply effects to game state declaratively"""
    if not effects:
        return state

    new_state = state.copy()

    # Handle trigger_event first
    if effects.get("trigger_event"):
        if effects["trigger_event"] == "free_traveler":
            new_state["event_flags"] = {
                **new_state.get("event_flags", {}),
                "helped_traveler": True
            }

    # Handle set_flag (both single flag and dictionary of flags)
    if effects.get("set_flag"):
        if isinstance(effects["set_flag"], dict):
            # Handle dictionary of multiple flags
            new_state["event_flags"] = {
                **new_state.get("event_flags", {}),
                **effects["set_flag"]
            }
        else:
            # Handle single flag
            new_state["event_flags"] = {
                **new_state.get("event_flags", {}),
                effects["set_flag"]: True
            }
    # Handle continue_to battle sequence
    if effects.get("continue_to"):
        new_state["continue_battle_from"] = effects["continue_to"]
        new_state["in_boss_battle"] = True

    # Handle battle trigger
    if effects.get("trigger_battle"):
        new_state["in_boss_battle"] = True
        new_state["location"] = "mountain_peak"  # Return to boss location

    # Handle item modifications
    if effects.get("remove_item"):
        new_state["inventory"] = [item for item in new_state["inventory"]
                                  if item != effects["remove_item"]]

    if effects.get("add_item"):
        new_state["inventory"] = new_state["inventory"] + [effects["add_item"]]

    # Handle exit unlocking - modified to directly update GAME_CONFIG
    if effects.get("unlock_exit") and effects.get("unlock_destination"):
        room_name = new_state["location"]
        if room_name in GAME_CONFIG["rooms"]:
            # Get current room config (don't make a copy - we want to modify original)
            room_config = GAME_CONFIG["rooms"][room_name]

            # Create new exits dictionary with the unlocked exit
            new_exits = {
                **room_config.get("exits", {}),
                effects["unlock_exit"]: effects["unlock_destination"]
            }

            # Update the room configuration directly in GAME_CONFIG
            room_config["exits"] = new_exits

            # Remove the obstacle since it's been overcome
            if "obstacle" in room_config:
                del room_config["obstacle"]

            # Also update collected_items if this is from picking up an item
            if "collected_items" in new_state:
                new_state["collected_items"] = list(set(new_state["collected_items"]))

    return new_state


def handle_movement(state: Dict, direction: str, current_config: Dict) -> Dict:
    """Handle player movement declaratively"""
    room = current_config["rooms"][state["location"]]

    # Check for maze obstacle first
    obstacle = room.get("obstacle")
    if obstacle and obstacle.get("direction") == direction:
        if room.get("movement_handler") == "maze":
            new_state = {
                **state,
                "location": state["location"],  # Stay in same room
                "maze_mode": True,
                "maze_position": room["maze"]["start"].copy()
            }
            return {
                "state": new_state,
                "output": obstacle["success_msg"],
                "config": current_config
            }
        else:
            # Handle non-maze obstacles here
            if obstacle.get("required_helper"):
                if not state["event_flags"].get(obstacle["required_helper"], False):
                    desc = obstacle.get("description", "You need help to overcome this obstacle.")
                    if callable(desc):
                        desc = desc(state)
                    return {"state": state, "output": desc, "config": current_config}

            # If helper requirement is met or not needed
            success_msg = obstacle.get("success_msg", "")
            if callable(success_msg):
                success_msg = success_msg(state)

            if "effects" in obstacle:
                new_state = apply_effects(state, obstacle["effects"])

                # Check if we should move the player after overcoming obstacle
                if obstacle["effects"].get("move_player", False):
                    destination = obstacle["effects"]["unlock_destination"]
                    new_state = {
                        **new_state,
                        "location": destination,
                        "just_entered": True
                    }

                    # For boss rooms, only return success message without description
                    if current_config["rooms"][destination].get("trigger_boss"):
                        return {
                            "state": new_state,
                            "output": success_msg,  # Just the climb success message
                            "config": current_config,
                            "trigger_boss": True
                        }

                    # For normal rooms, show both success message and description
                    dest_room = current_config["rooms"][destination]
                    dest_description = dest_room["description"]
                    if callable(dest_description):
                        dest_description = dest_description(new_state)

                    full_output = f"{success_msg}\n\n{dest_description}"

                    return {
                        "state": new_state,
                        "output": full_output,
                        "config": current_config
                    }

                return {
                    "state": new_state,
                    "output": success_msg,
                    "config": current_config
                }

    # Normal movement - check exits
    if direction in room.get("exits", {}):
        new_location = room["exits"][direction]
        new_visited = state["visited"] + [new_location] if new_location not in state["visited"] else state["visited"]
        new_state = {
            **state,
            "location": new_location,
            "visited": new_visited,
            "maze_mode": False,
            "just_entered": True
        }

        if current_config["rooms"][new_location].get("trigger_boss"):
            return {
                "state": new_state,
                "trigger_boss": True
            }

        return {"state": new_state, "config": current_config}

    return {"state": state, "output": "You can't go that way.", "config": current_config}


def respawn_player(state: Dict) -> Dict:
    """Respawn player at checkpoint declaratively"""
    print("\nYou feel your soul being pulled back...")
    print("You awaken at the echoing ledge. This is your checkpoint.\n")
    return {
        "state": {
            **state,
            "location": "echoing_ledge",
            "just_entered": True,
            "in_boss_battle": False,
            "continue_battle_from": None
        }
    }


def handle_maze_movement(state: Dict, direction: str, current_config: Dict) -> Dict:
    """Handle maze movement declaratively"""
    if not state.get("maze_mode"):
        return {"state": state, "output": "You're not in the maze.", "config": current_config}

    room = current_config["rooms"][state["location"]]
    maze = room["maze"]
    x, y = state["maze_position"]

    # Check if trying to exit maze (go behind from start position)
    if direction == "behind" and [x, y] == maze["start"]:
        new_state = {
            **state,
            "maze_mode": False
        }
        new_state.pop("maze_position", None)
        return {
            "state": new_state,
            "output": "You step back out of the maze entrance.",
            "config": current_config
        }

    # Calculate new position
    dx, dy = {
        "left": (0, -1),
        "right": (0, 1),
        "forward": (1, 0),
        "behind": (-1, 0)
    }.get(direction, (0, 0))

    new_x, new_y = x + dx, y + dy

    # Check bounds
    if not (0 <= new_x < len(maze["layout"]) or not (0 <= new_y < len(maze["layout"][0]))):
        return {"state": state, "output": "You bump into the rock wall.", "config": current_config}

    cell = maze["layout"][new_x][new_y]

    # Handle different cell types
    if cell == '#':
        return {"state": state, "output": "Solid stone blocks your path.", "config": current_config}
    elif cell == maze["trap_symbol"]:
        new_state = {**state, "maze_position": maze["start"].copy()}
        return {
            "state": new_state,
            "output": "A hidden trap snaps shut! You're jolted back to the start.",
            "config": current_config
        }
    elif cell == maze["exit_symbol"]:
        if "enchanted_sword" in state.get("collected_items", []):
            # Already have the sword
            new_state = {
                **state,
                "maze_mode": False,
                "maze_completed": True
            }
            new_state.pop("maze_position", None)
            return {
                "state": new_state,
                "output": "You reach the maze's end again. The stone pedestal stands empty, where the sword once rested.\n"
                          "You follow a tunnel returning you outside the maze",

                "config": current_config
            }
        else:
            # First time getting sword
            new_state = {
                **state,
                "maze_mode": False,
                "inventory": state["inventory"] + [room["reward_item"]],
                "maze_completed": True,
                "collected_items": state.get("collected_items", []) + [room["reward_item"]]
            }
            new_state.pop("maze_position", None)
            return {
                "state": new_state,
                "output":  "You've reached the end of the maze!\nBefore you stands an ornate pedestal holding an enchanted sword that hums with power.\n"
                        "The sword secured, you follow a tunnel returning you outside the maze",
                "config": current_config
            }

    # Update position for valid move
    new_state = {**state, "maze_position": [new_x, new_y]}

    # Describe available passages
    passages = []
    for dir_name, (dx, dy) in {
        "left": (0, -1),
        "right": (0, 1),
        "forward": (1, 0),
        "behind": (-1, 0)
    }.items():
        check_x, check_y = new_x + dx, new_y + dy
        if (0 <= check_x < len(maze["layout"]) and
                0 <= check_y < len(maze["layout"][0]) and
                maze["layout"][check_x][check_y] != '#'):
            passages.append(dir_name)
        elif dir_name == "behind" and [new_x, new_y] == maze["start"]:
            passages.append("behind")

    passage_text = (
        f"You see a passage to your {passages[0]}." if len(passages) == 1 else
        "You see passages to your " + ", ".join(passages[:-1]) + f" and {passages[-1]}." if passages else
        "There are no visible passages from here."
    )

    return {
        "state": new_state,
        "output": f"You move {direction} through the winding passage... {passage_text}",
        "config": current_config
    }


def handle_respawn(state: Dict) -> Dict:
    """Handle respawn command in maze"""
    if not state.get("maze_mode"):
        return {"output": "You can only respawn when in the maze."}

    return {
        "state": {
            **state,
            "maze_mode": False,
            "maze_position": None
        },
        "output": "You find yourself back at the maze entrance in the Whispering Cave."
    }


def handle_boss_battle(state: Dict) -> Dict:
    """Handle boss battle declaratively"""
    battle_config = GAME_CONFIG["boss_battle_outcomes"]

    while True:
        print("\nWhat will you do?")
        print("1. Fight\n2. Run\n3. Hide")
        choice = input("> ").strip()

        if choice == "1":
            result = handle_fight_sequence(state)
            if "state" in result:
                return result  # Return the state from fight sequence
            return {"state": state}  # Fallback return
        elif choice == "2":
            result = handle_run_sequence(state)
            if "state" in result:
                return result
            return {"state": state}
        elif choice == "3":
            result = handle_generic_sequence(state, battle_config["hide_sequence"])
            if "state" in result:
                return result
            return {"state": state}
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def handle_fight_sequence(state: Dict) -> Dict:
    """Handle fight sequence declaratively"""
    battle_state = "absorbed_heart" if state["event_flags"].get("absorbed_heart") else "no_heart"
    sequence = GAME_CONFIG["boss_battle_outcomes"]["fight_sequence"][battle_state]

    for step in ["cover_choices", "counter_choices", "final_choices"]:
        step_config = sequence[step]
        print("\n" + step_config["prompt"])

        while True:
            choice = input("> ").strip()
            if choice in step_config["options"]:
                outcome = step_config["options"][choice]

                for line in outcome.get("lines", []):
                    print(line)

                if "effects" in outcome:
                    new_state = apply_effects(state, outcome["effects"])

                    if outcome["effects"].get("fatal"):
                        return respawn_player(new_state)
                    if outcome["effects"].get("concludes"):
                        return handle_game_conclusion()
                    state = new_state
                break
            else:
                print("Invalid choice. Try again.")

    return {"state": state}


def handle_run_sequence(state: Dict) -> Dict:
    """Handle run sequence declaratively"""
    sequence = GAME_CONFIG["boss_battle_outcomes"]["run_sequence"]
    print("\n" + sequence["prompt"])

    while True:
        choice = input("> ").strip()
        if choice in sequence["options"]:
            option = sequence["options"][choice]

            for line in option.get("lines", []):
                print(line)

            if "effects" in option:
                new_state = apply_effects(state, option["effects"])

                # If we're continuing to battle, handle that immediately
                if option["effects"].get("continue_to"):
                    return {"state": new_state}  # Let game loop handle the continuation

                # Special handling for returning to battle
                if option["effects"].get("trigger_battle"):
                    print("\n" + GAME_CONFIG["rooms"]["mountain_peak"]["trigger_boss"]["prompt"])
                    return handle_boss_battle(new_state)

                return {"state": new_state}

            if "next" in option:
                next_step = option["next"]
                print("\n" + next_step["prompt"])

                while True:
                    nested_choice = input("> ").strip().lower()
                    if nested_choice in next_step["options"]:
                        nested_outcome = next_step["options"][nested_choice]

                        for line in nested_outcome.get("lines", []):
                            print(line)

                        if "effects" in nested_outcome:
                            new_state = apply_effects(state, nested_outcome["effects"])
                            if nested_outcome["effects"].get("fatal"):
                                return respawn_player(new_state)
                            if nested_outcome["effects"].get("concludes"):
                                return handle_game_conclusion()
                        return {"state": new_state}
                    else:
                        print("Please type 'yes' or 'no'.")

            return {"state": state}
        else:
            print("Invalid choice. Choose 1 or 2.")


def handle_run_battle_sequence(state: Dict) -> Dict:
    """Handle run battle sequence declaratively"""
    battle_state = "has_heart" if state["event_flags"].get("absorbed_heart") else "no_heart"
    sequence = GAME_CONFIG["boss_battle_outcomes"]["run_sequence"]["battle_sequence"]

    print("\n" + sequence["prompt"])
    print("1. Outwit Pyros\n2. Charge Together")

    while True:
        choice = input("> ").strip()
        if choice in sequence["options"][battle_state]:
            outcome = sequence["options"][battle_state][choice]

            for line in outcome.get("lines", []):
                print(line)

            if "effects" in outcome:
                if outcome["effects"].get("concludes"):
                    return handle_game_conclusion()
                if outcome["effects"].get("fatal"):
                    return respawn_player(state)

            return {"state": state}
        else:
            print("Invalid choice. Try again.")


def handle_generic_sequence(state: Dict, sequence: Dict) -> Dict:
    """Handle generic sequence declaratively"""
    print("\n" + sequence["prompt"])

    while True:
        choice = input("> ").strip()
        if choice in sequence["options"]:
            outcome = sequence["options"][choice]

            for line in outcome.get("lines", []):
                print(line)

            if "effects" in outcome:
                state = apply_effects(state, outcome["effects"])
                if outcome["effects"].get("fatal"):
                    return respawn_player(state)
                if outcome["effects"].get("concludes"):
                    return handle_game_conclusion()

            return {"state": state}
        else:
            print("Invalid choice. Try again.")


def handle_sequence_step(state: Dict, step_config: Dict) -> Dict:
    """Handle a single step in a battle sequence"""
    print("\n" + step_config["prompt"])

    while True:
        choice = input("> ").strip()
        if choice in step_config["options"]:
            outcome = step_config["options"][choice]

            for line in outcome.get("lines", []):
                print(line)

            if "effects" in outcome:
                new_state = apply_effects(state, outcome["effects"])
                if outcome["effects"].get("fatal"):
                    # Return both state and fatal flag
                    return {
                        "state": respawn_player(new_state)["state"],
                        "fatal": True
                    }
                if outcome["effects"].get("concludes"):
                    return handle_game_conclusion()
                return {"state": new_state}
            return {"state": state}
        else:
            print("Invalid choice. Try again.")

def handle_game_conclusion():
    """Handle game conclusion with complete game reset"""
    print("\nThank you for playing!")
    exit(0)

def respawn_player(state: Dict) -> Dict:
    """Respawn player at checkpoint declaratively"""
    print("\nYou feel your soul being pulled back...")
    print("You awaken at the echoing ledge. This is your checkpoint.\n")
    return {
        "state": {
            **state,
            "location": "echoing_ledge",
            "just_entered": True,  # To ensure room description shows again
            "in_boss_battle": False  # reset boss state
        }
    }


def handle_examine(state: Dict, item: str = None) -> Dict:
    """Handle examine command declaratively"""
    if not item:
        room = GAME_CONFIG["rooms"][state["location"]]

        # Handle dynamic description
        description = room["description"]
        if callable(description):
            description = description(state)

        output = f"\n{description}"

        # Handle dynamic items
        items = room.get("items", [])
        if callable(items):
            items = items(state)
        if items:
            output += "\nItems in room:\n" + "\n".join(f"- {i.replace('_', ' ')}" for i in items)

        return {"output": output}

    item_key = item.replace(" ", "_").lower()

    if item_key not in state["inventory"]:
        return {"output": "You don't have that item."}

    item_data = GAME_CONFIG["items"].get(item_key, {})
    output = f"\n{item_data.get('description', '')}"

    if "interaction" in item_data:
        interaction = item_data["interaction"]

        if "display" in interaction:
            output += f"\n{interaction['display']}"
            return {"output": output}

        print("\n" + interaction["prompt"])
        while True:
            choice = input("> ").strip().lower()
            if choice in interaction["options"]:
                outcome = interaction["options"][choice]

                for line in outcome.get("lines", []):
                    print(line)

                if "effects" in outcome:
                    new_state = apply_effects(state, outcome["effects"])
                    return {"state": new_state}
                break
            else:
                print(f"Please enter one of: {', '.join(interaction['options'].keys())}")

    return {"output": output}


def handle_take_item(state: Dict, item: str, current_config: Dict) -> Dict:
    """Handle take item command declaratively"""
    item_key = normalize_item_name(item)
    room = current_config["rooms"][state["location"]]

    # Get current items (handling both list and callable)
    current_items = room["items"](state) if callable(room.get("items")) else room.get("items", [])

    if item_key in current_items:
        new_inventory = state["inventory"] + [item_key]
        new_collected = state.get("collected_items", []) + [item_key]

        output = f"You take the {item.replace('_', ' ')}."

        if "upon_take" in current_config["items"].get(item_key, {}):
            output += f"\n\n{current_config['items'][item_key]['upon_take']}"

        # Special case for maze reward
        if state.get("location") == "whispering_cave" and item_key == "enchanted_sword":
            return {
                "state": {
                    **state,
                    "inventory": new_inventory,
                    "collected_items": new_collected,
                    "maze_completed": True
                },
                "output": output
            }

        return {
            "state": {
                **state,
                "inventory": new_inventory,
                "collected_items": new_collected
            },
            "output": output
        }

    return {"output": "There is no such item here."}


def handle_use_item(state: Dict, item_name: str, current_config: Dict) -> Dict:
    """Handles using an item."""
    if item_name not in state["inventory"]:
        return {"state": state, "output": f"You don't have the {item_name.replace('_', ' ')}."}

    current_room = current_config["rooms"][state["location"]]
    obstacle = current_room.get("obstacle")

    if not obstacle:
        return {"state": state, "output": "There's nothing here to use that on."}

    # Handle helper-based obstacles (like the high ledge)
    if obstacle.get("required_helper"):
        if not state["event_flags"].get(obstacle["required_helper"], False):
            # Get obstacle description (handling both string and callable)
            desc = obstacle.get("description", "You need help to overcome this obstacle.")
            if callable(desc):
                desc = desc(state)
            return {"state": state, "output": desc}

        # Helper is available - overcome obstacle
        print(obstacle["success_msg"])
        new_state = apply_effects(state, obstacle.get("effects", {}))

        # Remove obstacle after successful use if needed
        if "obstacle" in current_room:
            del current_room["obstacle"]

        return {"state": new_state, "config": current_config}

    # Handle item-based obstacles (like the gate with relic)
    if obstacle.get("required_item") == item_name:
        # Check if additional helper is required
        if obstacle.get("required_helper") and not state["event_flags"].get(obstacle["required_helper"], False):
            desc = obstacle.get("description", "You need help to use that here.")
            if callable(desc):
                desc = desc(state)
            return {"state": state, "output": desc}

        print(obstacle["success_msg"])
        new_state = apply_effects(state, obstacle.get("effects", {}))

        # Remove obstacle after successful use if needed
        if "obstacle" in current_room:
            del current_room["obstacle"]

        return {"state": new_state, "config": current_config}

    return {"state": state, "output": f"The {item_name.replace('_', ' ')} has no effect here."}


def render_map(current_location: str) -> str:
    """Render ASCII map declaratively"""

    def mark(name):
        return f"[{name}]<--" if name == current_location else f"[{name}]"

    return f"""
                         {mark("mountain_peak")}
                                 |
     {mark("whispering_cave")}   {mark("echoing_ledge")}
                 \\       /
               {mark("deep_cave")}
                   |
     {mark("glowing_cave")}  {mark("shrouded_path")}
                 \\       /
              {mark("forest_entry")}
"""


def save_game(state: Dict):
    """Saves the current game state to a JSON file."""
    try:
        # Create a snapshot of the current room configurations that have been modified
        saved_rooms = {}
        for room_name, room_config in GAME_CONFIG["rooms"].items():
            # Only save rooms that have modified exits
            if "exits" in room_config and len(room_config["exits"]) > 0:
                saved_rooms[room_name] = {"exits": room_config["exits"]}

        # Include the room configurations in the saved state
        full_state = {
            **state,
            "saved_rooms": saved_rooms
        }

        with open(SAVE_FILE, "w") as f:
            json.dump(full_state, f, indent=4)
        return {"output": "Game saved successfully!"}
    except Exception as e:
        return {"output": f"Error saving game: {e}"}

def load_game(default_state: Dict) -> Dict:
    """Loads the game state from a JSON file, merging with default values."""
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                loaded_state = json.load(f)

            # Create a new state dictionary
            merged_state = default_state.copy()

            # Restore basic state fields
            for key in ["location", "inventory", "visited", "event_flags",
                       "maze_mode", "maze_position", "collected_items"]:
                if key in loaded_state:
                    merged_state[key] = loaded_state[key]

            # Restore room configurations if they were saved
            if "saved_rooms" in loaded_state:
                for room_name, room_data in loaded_state["saved_rooms"].items():
                    if room_name in GAME_CONFIG["rooms"]:
                        GAME_CONFIG["rooms"][room_name]["exits"] = room_data["exits"]

            return {"state": merged_state, "output": "Game loaded successfully!"}

        except json.JSONDecodeError:
            return {"state": default_state, "output": "Error loading save file. Starting new game."}
        except Exception as e:
            return {"state": default_state, "output": f"An error occurred loading game: {e}. Starting new game."}
    else:
        return {"state": default_state, "output": "No save file found. Starting new game."}


def normalize_item_name(item_name: str) -> str:
    """Convert item names with spaces to use underscores consistently"""
    return item_name.strip().replace(" ", "_").lower()

# ========== GAME LOOP ==========

def game_loop(initial_state=None):
    """Main game loop with configurable initial state"""
    print(GAME_CONFIG["intro_text"])
    print("Type 'help' to see controls.")

    state = initial_state if initial_state else GAME_CONFIG["initial_state"].copy()
    current_config = {**GAME_CONFIG}

    while True:
        # Show room description if we're in a normal room and just entered
        if state.get("just_entered") and state["location"] in current_config["rooms"]:
            room = current_config["rooms"][state["location"]]
            if "description" in room:
                description = room["description"]
                if callable(description):
                    description = description(state)
                print(f"\n{description}")

                items = room.get("items", [])
                if callable(items):
                    items = items(state)
                if items:
                    print("Items in room:")
                    for item in items:
                        print(f"- {item.replace('_', ' ')}")

            state["just_entered"] = False

        try:
            # Handle continued battle sequence before accepting new input
            if state.get("continue_battle_from"):
                battle_state = "absorbed_heart" if state["event_flags"].get("absorbed_heart") else "no_heart"
                sequence = GAME_CONFIG["boss_battle_outcomes"]["fight_sequence"][battle_state]
                start_from = state["continue_battle_from"]
                state["continue_battle_from"] = None  # Clear it immediately

                if start_from == "cover_choices":
                    print("\nPyros roars as you return to the battle!")
                    result = handle_sequence_step(state, sequence["cover_choices"])
                    if "state" in result:
                        state = result["state"]
                        if result.get("fatal"):
                            continue  # Skip rest if fatal

                        result = handle_sequence_step(state, sequence["counter_choices"])
                        if "state" in result:
                            state = result["state"]
                            if result.get("fatal"):
                                continue  # Skip rest if fatal

                            result = handle_sequence_step(state, sequence["final_choices"])
                            if "state" in result:
                                state = result["state"]
                continue

            user_input = input("\n> ").strip().lower()
            if not user_input:
                continue

            if user_input == "quit":
                print("Goodbye.")
                break

            parts = user_input.split()
            command = parts[0]
            args = parts[1:] if len(parts) > 1 else []

            # Handle respawn command
            if command == "respawn":
                if state.get("maze_mode"):
                    state["maze_mode"] = False
                    state["maze_position"] = None
                    print("You find yourself back at the maze entrance in the Whispering Cave.")
                    continue
                else:
                    print("You can only respawn when in the maze.")
                    continue

            # Normalize command input
            if command in ["use", "take", "examine"] and args:
                args = [normalize_item_name(" ".join(args))]

            # Handle commands
            if command in current_config["commands"]:
                if command in ["examine", "take", "use"] and not args and command != "examine":
                    print(f"Usage: {command} [target]")
                    continue

                if command == "examine":
                    if not args:
                        if state["location"] not in current_config["rooms"]:
                            result = {"output": "Focus on the battle!"}
                        else:
                            room = current_config["rooms"][state["location"]]
                            if "description" in room:
                                description = room["description"]
                                if callable(description):
                                    description = description(state)
                                result = {"output": f"\n{description}"}
                            else:
                                result = {"output": "You look around but see nothing noteworthy."}

                            items = room.get("items", [])
                            if callable(items):
                                items = items(state)
                            if items:
                                result["output"] += "\nItems in room:\n" + "\n".join(
                                    f"- {i.replace('_', ' ')}" for i in items)
                    else:
                        result = current_config["commands"][command]["action"](state, args[0])
                elif command in ["take", "use", "go"]:
                    result = current_config["commands"][command]["action"](state, *args, current_config)
                elif command in ["inventory", "map", "save", "load", "help"]:
                    result = current_config["commands"][command]["action"](state)
                else:
                    result = {"output": "Command not properly configured."}

            # Handle movement commands
            elif command in ["forward", "back", "left", "right", "behind", "go"]:
                direction = args[0] if command == "go" else command

                if state.get("maze_mode"):
                    result = handle_maze_movement(state, direction, current_config)
                else:
                    result = current_config["commands"]["go"]["action"](state, direction, current_config)
                    if "state" in result and result["state"]["location"] != state["location"]:
                        result["state"]["just_entered"] = True
            else:
                print("Invalid command. Type 'help' for options.")
                continue

            # Update state and config
            if "state" in result:
                state = result["state"]

            if "config" in result:
                current_config = result["config"]

            if "output" in result:
                print(result["output"])

            if "room_update" in result and state["location"] in current_config["rooms"]:
                current_config["rooms"][state["location"]] = {
                    **current_config["rooms"][state["location"]],
                    **result["room_update"]
                }

            # Handle boss triggers
            if "trigger_boss" in result and result["trigger_boss"]:
                print("\n" + GAME_CONFIG["rooms"]["mountain_peak"]["trigger_boss"]["prompt"])
                boss_result = handle_boss_battle(state)
                if "state" in boss_result:
                    state = boss_result["state"]
                    state["just_entered"] = True

        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    game_loop()
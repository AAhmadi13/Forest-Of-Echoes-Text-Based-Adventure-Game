import json
import os


# --- INTRODUCTION TEXT ---
intro_text = """
The Forest of Echoes whispers your name, Alex.

You've come alone, driven by the legend of the Crown of Pyros — a treasure said to hold the power to bend fate itself.  
Your path leads to the summit of Mount Duskveil, where the treasure waits beyond shadows and ancient trials.

Every step you take echoes with danger and secrets long forgotten.

Trust no one, rely on your wits, and prepare to face the unknown.

Your journey begins now.
"""


def print_intro():
    print(intro_text)

boss_battle_outcomes = {
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
                    "fatal": True
                },
                    "2": {
                        "lines": [
                            "\nYou dive behind rubble, but suffer severe burns on your right hand.",
                            "Your right hand is injured and weak. You won't be able to wield your sword as effectively."
                        ],
                    },
                    "3": {
                        "lines": [
                            "\nYou take shelter behind a solid rock wall, shielded from the fire."
                        ],
                    }
                }
            },
            "counter_choices": {
                "prompt": "Pyros, enraged by your escape, charges toward you!\n1. Dodge\n2. Strike with your sword",
                "options": {
                    "1": [
                        "\nYou quickly dodge to the side, narrowly avoiding Pyros' charge.",
                        "The dragon takes to the sky and begins circling above."
                    ],
                    "2": [
                        "\nYou swing your sword at the charging dragon!",
                        "It's a direct hit, but the recoil throws you backward as Pyros takes to the sky."
                    ]
                }
            },
            "final_choices": {
            "prompt": "The dragon circles above. Choose your final move:\n1. Time your strike and leap with your sword\n2. Run to the crown and escape\n3. Signal the traveler to help distract Pyros",
            "options": {
                "1": {
                    "lines": ["\nYou leap with your sword, plunging it into Pyros as he dives.",
                    "The beast crashes into the mountain, but not before impaling you in flame.",
                    "The traveler catches your body as the world darkens.",
                    "\n💀 THE END – A Hero's Sacrifice 💀"
                    ],
                    "fatal": True
                },
                "2": {
                    "lines": [
                    "\nYou sprint to the Crown of Pyros and grab it as you flee.",
                    "The dragon crashes into the summit behind you, crushing the traveler in a blaze.",
                    "You have the crown, but at the cost of everything else.",
                    "\n🏅 THE END – Crown Without Power 🏅"
                    ],
                    "concludes": True
                },
                "3": {
                    "lines": [
                    "\nYou signal to the traveler. He nods and rushes to the side, hurling rocks and shouting.",
                    "Pyros turns his attention momentarily. You seize the opening and charge forward!",
                    "With a perfectly timed leap, you plunge the enchanted sword deep into the dragon’s heart.",
                    "It thrashes, roaring in pain... and collapses.",
                    "Smoke rises. You and the traveler fall to your knees, exhausted but alive.",
                    "You and the traveler claim the legendary Crown of Pyros.",
                    "\n🏆 THE END – Dragon Slayer 🏆"
                    ],
                    "concludes": True
                }
            }
            }
        },
        "absorbed_heart": {
                "cover_choices": {
                    "prompt": "Pyros roars and unleashes a stream of fire! Where do you take cover?\n1. Stand your ground\n2. Conjure a barrier\n3. Dash behind enchanted rocks",
                    "options": {
                        "1": [
                            "\nSuddenly, you feel a surge of energy! The Heart's power courses through you.",
                            "Your burned arm begins to heal rapidly, and you feel lightning coursing through your veins.",
                            "You stand firm as the flames approach. The heart within you pulses brightly, shielding you in a fiery aura.",
                            "You are unharmed. Pyros growls in confusion."
                        ],
                        "2": [
                            "\nYou conjure a barrier using the heart's energy. The flames part around you.",
                            "The traveler watches in awe as your eyes glow crimson."
                        ],
                        "3": [
                            "\nYou and the traveler dive behind glowing rocks. The flames strike, but the rocks hold firm.",
                            "\nYou feel the Heart's power surging through you, lightning coursing through your veins.",
                            "You raise your hand and unleash a powerful lightning blast at Pyros!",
                            "The dragon roars in pain as the lightning strikes its scales."
                        ]
                    }
                },
                "counter_choices": {
                    "prompt": "Pyros charges toward you! The heart pulses with power.\n1. Blast Pyros with energy\n2. Dodge and empower your blade",
                    "options": {
                        "1": [
                            "\nYou release a burst of raw energy from your palm, striking Pyros mid-charge.",
                            "He reels back, scales charred, as he takes to the skies."
                        ],
                        "2": [
                            "\nYou dodge and channel the heart's power into your sword. It glows with ghostly fire.",
                            "You are ready for the final blow."
                        ]
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
                            "concludes": True
                        },
                        "2": {
                            "lines": [
                            "\nYou summon chains of spirit flame that yank Pyros from the sky.",
                            "He lands with a thunderous crash, subdued and broken.",
                            "The traveler gasps. 'What... what are you becoming?'",
                            "\n👻 THE END – Master of the Heart 👻"
                            ],
                            "concludes": True
                        }
                    }
                }
        }
    },
    "run_sequence": {
        "prompt": "You flee the battlefield. The traveler runs with you but suddenly stumbles and falls behind.\nDo you go back to help or keep running?\n1. Help the traveler\n2. Keep running",
        "options": {
            "1": [
                "\nYou run back and lift the traveler just as Pyros' flame scorches the trees.",
                "Together, you duck behind a ridge. The traveler looks at you, grateful but wounded.",
                "He hands you a dagger and nods. 'Let’s end this.'",
                "\nYou both return to face Pyros, scarred but determined.",
                "(Continue to the battle sequence.)"
            ],
            "2": [
                "\nYou leave the traveler behind. You find refuge in a forest and a witch's hut.",
                "Inside, a cup of water sits on the table. Do you drink it?"
            ],
            "drink_decision": {
                "yes": {
                    "lines" : [
                    "\nYou drink the water, feeling a strange sensation. Your vision begins to blur...",
                    "💀 THE END – Poisoned by the Witch 💀"
                    ],
                    "fatal" : True
                },
                "no": {
                    "lines" : [
                    "\nYou decide not to drink the water. Exhausted, you lie down on the witch's bed and fall asleep.",
                    "You wake up tied to a chair, the witch standing over you with a wicked smile.",
                    "💀 THE END – Caught by the Witch 💀"
                    ],
                    "fatal" : True
                }
            }
        },
        "battle_sequence": {
            "prompt": "Pyros roars and prepares to strike. How do you proceed?",
            "options": {
                "no_heart": {
                    "1": {
                        "lines": [
                        "\nYou lure Pyros toward a cliff edge.",
                        "The traveler throws rocks to bait the dragon.",
                        "Pyros loses balance and crashes into the abyss.",
                        "You and the traveler claim the legendary Crown of Pyros.",
                        "\n🏅 THE END – Outwitted the Flame 🏅"
                        ],
                        "concludes": True
                    },
                    "2": {
                        "lines": [
                        "\nYou and the traveler charge head-on.",
                        "Pyros' flames catch the traveler, but you strike hard.",
                        "Despite your efforts, Pyros overwhelms you both.",
                        "\n💀 THE END – Brave, But Overpowered 💀"
                        ],
                        "fatal": True
                    }
                },
                "has_heart": {
                    "1": {
                        "lines": [
                            "\nYou channel energy into the dagger and hand it to the traveler.",
                            "He throws it into Pyros' eye.",
                            "You finish Pyros with a powerful strike.",
                            "\n👑 THE END – Shared Glory 👑"
                        ],
                        "concludes": True
                    },
                    "2": {
                        "lines": [
                            "\nYou summon lightning and strike from above.",
                            "Pyros is vaporized in a blinding blaze.",
                            "The traveler watches in awe as silence returns.",
                            "Together, you claim the legendary Crown of Pyros, its power now yours.",
                            "\n👻 THE END – God of the Storm 👻"
                        ],
                        "concludes": True
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
                "fatal": True
            },
            "2": {
                "lines": [
                    "\nYou jump from the tree, landing awkwardly on a hidden trap.",
                    "Spikes impale your legs.",
                    "\n💀 THE END – Impaled 💀"
                ],
                "fatal": True
            }
        }
    },
}



# Room definitions
rooms = {
    "forest_entry": {
        "description": "You stand at the edge of the Forest of Echoes. Mist clings to the ground. Paths stretch left and right.",
        "exits": {"left": "glowing_cave", "right": "shrouded_path"},
        "items": []
    },
    "glowing_cave": {
        "description": "Blue crystals pulse in the cave walls. A sealed gate blocks your path forward.",
        "exits": {"right": "forest_entry"},
        "items": [],
        "obstacle": {
            "name": "gate",
            "required_item": "relic",
            "success_msg": "The relic glows and unlocks the gate. The path forward is now open.",
            "unlock_exit": "forward",
            "unlock_destination": "deep_cave"
        }
    },
    "shrouded_path": {
        "description": "A wounded traveler lies unconscious against a twisted tree, entangled in thick, living vines.\nA faint glint catches your eye — a relic lies near his hand, likely dropped before he collapsed.\nThe vines look tough... you'll need something sharp to cut him free.",
        "exits": {"left": "forest_entry"},
        "items": ["relic"],
        "obstacle": {
                "name": "vines",
                "required_item": "enchanted_sword",
                "success_msg": "You slash the vines with your sword. The traveler gasps in relief and thanks you. He now joins you as a companion.",
                "trigger_event": "free_traveler"
        },
        "event": "traveler"
    },
    "deep_cave": {
        "description": "The Heart of Yurei floats above a stone altar, pulsing with silent energy, beckoning you to \033[1mtake it\033[0m.",
        "exits": {"behind": "glowing_cave", "left": "whispering_cave", "right": "echoing_ledge"},
        "items": ['heart_of_yurei']
    },
    "whispering_cave": {
        "description": "You're at the mouth of a massive underground maze carved into the cavern wall.\nThe air is dense, and the echo of dripping water mixes with distant whispers.",
        "exits": {"right": "deep_cave"},
        "obstacle": {
                "name": "maze_entry",
                "required_item": None,
                "direction": "forward",
                "success_msg": "You step cautiously into the twisting maze ahead, the stone walls closing in around you."
        },
        "movement_handler": "maze",  # Used to determine custom movement logic
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
            "start": [0, 5],
            "exit_symbol": "E",
            "trap_symbol": "T"
        },
        "maze_completed": False,
        "reward_item": "enchanted_sword"
    },
    "echoing_ledge": {
        "description": (
            "This narrow chamber hums with energy. In front of you, a dusty stone pedestal holds a rolled-up parchment — its surface faintly glowing.\nTo your right, a steep rock face rises high — too far to climb alone."
        ),
        "exits": {"left": "deep_cave"},
        "items": ["maze_map"],
        "obstacle": {
            "name": "high_ledge",
            "description": "A high ledge blocks your way up. You’ll need help to reach it.",
            "required_helper": "traveler",
            "unlock_exit": "right",
            "unlock_destination": "mountain_peak",
            "success_msg": "With the traveler's help, you scale the high ledge to the mountain peak."
        },
    },
    "mountain_peak": {
        "description": ( "You stand atop the scorched summit of Mount Duskveil.\nBefore you looms the colossal Fire Dragon, Pyros, its scales glowing like molten lava.\nThe legendary Crown of Pyros rests upon a rock altar behind the beast, radiating power.\nThis is the final confrontation. Your choices now will shape your fate.\n🔥 FINAL BATTLE – The Fire Dragon Pyros awakens! 🔥\nThe ground trembles. Smoke rises. You must decide:"
        ),
        "exits": {},
        "trigger_boss": True
    }
}

# Items descriptions/interactive
items = {
    "relic": {
        "description": "An ancient relic pulsing with a soft, ethereal light. It seems to react to nearby energy."
    },
    "crown_of_pyros": {
        "description": "The mythical Crown of Pyros, forged from dragonfire and set with eternal rubies. It symbolizes triumph over the beast."
    },
    "heart_of_yurei": {
        "description": "A glowing, pulsating heart-shaped crystal. It hums with latent power waiting to be awakened.",
        "upon_take": "The Heart of Yurei pulses warmly in your hand, filling you with strange energy.\nAs you hold the Heart, you feel a strange connection to it. You should examine it more closely.",
        "interaction_on_examine": {
        "prompt": "Do you want to absorb it or put it away? (absorb/put away): ",
            "options": ["absorb", "put away"],
            "outcomes": {
                "absorb": {
                    "prompt": (
                        "As you hold the Heart close to your chest, it begins to glow intensely.\n"
                        "The crystal-like surface starts to shimmer and dissolve into pure energy.\n"
                        "You feel a warm sensation as the Heart fuses with your body, entering your chest.\n"
                        "A wave of energy courses through your veins, and your vision begins to blur...\n\n"
                        "[6 hours later]\n\n"
                        "You slowly regain consciousness, your body tingling with newfound energy.\n"
                        "A warm, electrifying sensation courses through your body, as if lightning flows in your blood.\n"
                        "The Heart of Yurei has become one with you, its power now a part of your very being."
                    ),
                    "effects": {
                        "absorbed_heart": True,
                        "remove_from_inventory": True
                    }
                },
                "put away": {
                        "prompt": "You carefully place the Heart in your bag, feeling its gentle pulse against your side.",
                        "effects": {}
                }
            }
        }
    },
    "maze_map": {
        "description": "A faded parchment showing the maze layout. Key turns are marked in red pigment — a clear guide through the Whispering Maze.",
        "interaction_on_examine": {
                "prompt": (
                    "You unfold the parchment and study the sketch:\n\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # | # | # | # | # | # | # | # | # | # | # | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # | T |   |   |   |   |   |   |   |   | E | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # | # | # | # |   | # | # | # |   | # |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # | T |   |   |   | # |   |   |   |   |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # | # | # |   | # | # |   | # | # | # |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # |   |   |   |   |   |   | # |   |   |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # |   | # | # |   | # | # | # |   | # |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # |   | # | T |   | # |   |   |   | # |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # |   | # | # |   | # |   | # |   | # |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # |   | T | # |   | S |   | # |   |   |   | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n"
                    "| # | # | # | # | # | ↓ | # | # | # | # | # | # |\n"
                    "+---+---+---+---+---+---+---+---+---+---+---+---+\n\n"
                    "S = Start, ↓ = Retreat (Return to Cave), T = Trap, E = Exit, # = Wall"

                ),
                "effects": []
        }
    },
    "enchanted_sword": {
        "description": ""
    }
}


# Player state
player_state = {
    "location": "forest_entry",
    "inventory": [],
    "visited": ["forest_entry"],
    "event_flags": {
        "helped_traveler": False,
        "took_heart": False,
        "absorbed_heart": False,
        "right_hand_injured": False
    },
    "maze_mode": False,
    "maze_position": None
}

SAVE_FILE = "savegame.json"


# ----- Handlers

# ----- Final boss related handlers -----

def handle_final_boss(player_state):
    while True:
        initial_choice = input("\nWhat will you do?\n1. Fight\n2. Run\n3. Hide\n> ").strip()
        if initial_choice == "1":
            return handle_fight_sequence(player_state)
        elif initial_choice == "2":
            return handle_run_sequence(player_state)
        elif initial_choice == "3":
            return handle_generic_sequence(boss_battle_outcomes["hide_sequence"], player_state)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def handle_fight_sequence(player_state):
    state = "absorbed_heart" if player_state["event_flags"].get("absorbed_heart") else "no_heart"
    sequence = boss_battle_outcomes["fight_sequence"][state]

    for step in ["cover_choices", "counter_choices", "final_choices"]:
        prompt = sequence[step]["prompt"]
        options = sequence[step]["options"]

        while True:
            print("\n" + prompt)
            choice = input("> ").strip()
            if choice in options:
                if process_outcome(options[choice], player_state):
                    return  # Player died, respawn handled
                if isinstance(options[choice], dict) and options[choice].get("concludes"):
                    # Game concludes successfully
                    print("\nThank you for playing!")
                    exit(0)
                break
            else:
                print("Invalid choice. Try again.")

def respawn_player_at_checkpoint(player_state):
    print("\nYou feel your soul being pulled back...")
    print("You awaken at the echoing ledge. This is your checkpoint.\n")
    player_state["location"] = "echoing_ledge"


def handle_run_sequence(player_state):
    run_seq = boss_battle_outcomes["run_sequence"]
    print("\n" + run_seq["prompt"])

    while True:
        choice = input("> ").strip()
        options = run_seq["options"]

        if choice == "1":
            if process_outcome(options["1"], player_state):
                return
            player_state["event_flags"]["helped_traveler"] = True
            return handle_run_battle_sequence(player_state)

        elif choice == "2":
            if process_outcome(options["2"], player_state):
                return

            while True:
                drink_choice = input("Do you want to drink the water? (yes/no): ").strip().lower()
                if drink_choice in options["drink_decision"]:
                    if process_outcome(options["drink_decision"][drink_choice], player_state):
                        return
                    return
                else:
                    print("Please type 'yes' or 'no'.")
        else:
            print("Invalid choice. Choose 1 or 2.")


def handle_run_battle_sequence(player_state):
    state = "has_heart" if player_state["event_flags"].get("absorbed_heart") else "no_heart"
    battle_seq = boss_battle_outcomes["run_sequence"]["battle_sequence"]

    print("\n" + battle_seq["prompt"])
    print("1. Outwit Pyros\n2. Charge Together")

    while True:
        choice = input("> ").strip()
        if choice in battle_seq["options"][state]:
            if process_outcome(battle_seq["options"][state][choice], player_state):
                return
            if isinstance(battle_seq["options"][state][choice], dict) and battle_seq["options"][state][choice].get("concludes"):
                print("\nThank you for playing!")
                exit(0)
            return
        else:
            print("Invalid choice. Try again.")


def handle_generic_sequence(sequence, player_state):
    print("\n" + sequence["prompt"])
    while True:
        choice = input("> ").strip()
        if choice in sequence["options"]:
            if process_outcome(sequence["options"][choice], player_state):
                return
            if isinstance(sequence["options"][choice], dict) and sequence["options"][choice].get("concludes"):
                print("\nThank you for playing!")
                exit(0)
            return
        else:
            print("Invalid choice. Try again.")


def process_outcome(outcome, player_state):
    lines = outcome["lines"] if isinstance(outcome, dict) else outcome
    for line in lines:
        print(line)
    if isinstance(outcome, dict):
        if outcome.get("fatal"):
            respawn_player_at_checkpoint(player_state)
            return True  # Indicate the player died
        if outcome.get("concludes"):
            # Handle conclusion (no respawn, just end)
            print("\nThe battle has concluded.")
            return "concludes"  # special signal for conclusion
    return False



# ------------

def handle_ledge_climb():
    location = player_state["location"]
    room = rooms[location]

    obstacle = room.get("obstacle")
    if obstacle and obstacle.get("name") == "high_ledge":
        if player_state["event_flags"].get("helped_traveler"):
            print("With the traveler's help, you climb the high ledge with ease.")
            # Unlock exit to next room (example: "up" → "mountain_peak")
            room["exits"]["up"] = "mountain_peak"
            del room["obstacle"]
        else:
            print(obstacle.get("description", "The ledge is too high to climb alone."))


def handle_free_traveler():
    player_state["event_flags"]["helped_traveler"] = True

def handle_maze_movement(direction, room):
    if not player_state.get("maze_mode", False):
        player_state["maze_mode"] = True
        player_state["maze_position"] = room["maze"]["start"]
    else:
        pos = player_state.get("maze_position", room["maze"]["start"])

    # Handle local 'respawn' command to exit maze
    if direction == "respawn":
        player_state["location"] = "whispering_cave"
        player_state["maze_mode"] = False
        player_state.pop("maze_position", None)
        return "You whisper 'respawn' and feel a strange tug... In a blink, you're back in the Whispering Cave."

    x, y = player_state["maze_position"]
    dx, dy = {
        "left": (0, -1),
        "right": (0, 1),
        "forward": (1, 0),
        "behind": (-1, 0)
    }.get(direction, (0, 0))

    # Exit maze if going behind from start
    if direction == "behind" and [x, y] == room["maze"]["start"]:
        player_state["location"] = "whispering_cave"
        player_state["maze_mode"] = False
        player_state.pop("maze_position", None)
        return "You step back from the maze and return to the Whispering Cave."

    new_x, new_y = x + dx, y + dy
    layout = room["maze"]["layout"]

    if not (0 <= new_x < len(layout) and 0 <= new_y < len(layout[0])):
        return "You bump into the rock wall — no passage that way."

    cell = layout[new_x][new_y]
    if cell == '#':
        return "Solid stone blocks your path."
    elif cell == room["maze"]["trap_symbol"]:
        player_state["maze_position"] = room["maze"]["start"]
        return "A hidden trap snaps shut beneath your feet! You're jolted back to the start."
    elif cell == room["maze"]["exit_symbol"]:
        room["maze_completed"] = True
        player_state["maze_mode"] = False
        player_state.pop("maze_position", None)
        reward_item = room.get("reward_item")
        if reward_item and reward_item not in player_state["inventory"]:
            player_state["inventory"].append(reward_item)
        room["exits"]["right"] = "deep_cave"
        return f"You've reached the end of the maze and claim the {reward_item.replace('_', ' ')} lying on a pedestal! A path opens back to the deep cave."

    player_state["maze_position"] = [new_x, new_y]

    directions = {
        "left": (0, -1),
        "right": (0, 1),
        "forward": (1, 0),
        "behind": (-1, 0)
    }

    available_passages = []
    for dir_name, (dx_check, dy_check) in directions.items():
        check_x, check_y = new_x + dx_check, new_y + dy_check
        if dir_name == "behind" and [new_x, new_y] == room["maze"]["start"]:
            # Special case: prompts behind even though it's out of bounds, to exit maze
            available_passages.append("behind")
        elif 0 <= check_x < len(layout) and 0 <= check_y < len(layout[0]):
            if layout[check_x][check_y] != '#':
                available_passages.append(dir_name)

    if available_passages:
        if len(available_passages) == 1:
            passages_text = f"You see a passage to your {available_passages[0]}."
        else:
            last = available_passages[-1]
            others = available_passages[:-1]
            passages_text = "You see passages to your " + ", ".join(others) + f" and {last}."
    else:
        passages_text = "There are no visible passages from here."

    return f"You move {direction} through the winding passage... {passages_text}"
# -------

def save_game():
    with open(SAVE_FILE, "w") as f:
        json.dump(player_state, f)
    print("Game saved.")


def load_game():
    global player_state
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            player_state = json.load(f)
        print("Game loaded.")
    else:
        print("No saved game found.")


def print_help():
    print("""
Commands:
- left, right, forward, behind: Move in directions
- examine [item]: Examine current room or an item in your inventory
- take [item]: Pick up an item
- inventory: View your items
- use [item]: Use an item in the current location
- save: Save the game
- load: Load saved game
- map: View an ASCII map
- help: Show this help message
- quit: Exit the game
""")

def move_player(direction):
    location = player_state["location"]
    room = rooms[location]

    # Handle 'respawn' command inside maze mode only
    if direction == "respawn":
        if player_state.get("maze_mode", False):
            result = handle_maze_movement("respawn", room)
            print(result)
        else:
            print("You whisper 'respawn', but nothing happens here.")
        return

    obstacle = room.get("obstacle")

    # Maze entry logic (declarative)
    if obstacle:
        if obstacle.get("name") == "maze_entry" and obstacle.get("direction") == direction:
            if not player_state.get("maze_mode", False):
                player_state["maze_mode"] = True
                player_state["maze_position"] = room["maze"]["start"]
                print(obstacle["success_msg"])
            result = handle_maze_movement(direction, room)
            print(result)
            return

    # Maze movement mode handler
    if room.get("movement_handler") == "maze" and player_state.get("maze_mode", False):
        result = handle_maze_movement(direction, room)
        print(result)
        return

    # Obstacle-based unlock (declarative high ledge logic)
    if obstacle:
        unlock_dir = obstacle.get("unlock_exit")
        unlock_dest = obstacle.get("unlock_destination")
        required_helper = obstacle.get("required_helper")

        if unlock_dir == direction and unlock_dest and unlock_dir not in room["exits"]:
            if required_helper and not player_state["event_flags"].get(f"helped_{required_helper}"):
                print(obstacle.get("description", "You can't proceed that way yet."))
                return
            room["exits"][unlock_dir] = unlock_dest
            print(obstacle.get("success_msg", "You overcame the obstacle."))

    # Standard directional movement
    if direction in room.get("exits", {}):
        destination = room["exits"][direction]
        player_state["location"] = destination

        if destination not in player_state["visited"]:
            player_state["visited"].append(destination)

        new_room = rooms[destination]
        if new_room.get("on_enter_effect") and new_room.get("obstacle", {}).get("name") == "high_ledge":
            handle_ledge_climb()

        examine()

        # boss battle trigger
        if new_room.get("trigger_boss"):
            handle_final_boss(player_state)
    else:
        print("You can't go that way.")



def use_item(item):
    location = player_state["location"]
    room = rooms[location]

    item_key = item.replace(" ", "_").lower()

    if item_key not in player_state["inventory"]:
        print(f"You don't have the {item}.")
        return

    obstacle = room.get("obstacle")
    if obstacle and obstacle.get("required_item") == item_key:
        print(obstacle.get("success_msg", ""))

        # Optionally unlock exits if defined (not always needed)
        if "unlock_exit" in obstacle and "unlock_destination" in obstacle:
            room["exits"][obstacle["unlock_exit"]] = obstacle["unlock_destination"]

        # Directly call the handler / trigger event-based effects
        if obstacle.get("name") == "vines":
            handle_free_traveler()

        # Remove the obstacle
        del room["obstacle"]
    else:
        print("Using that here has no effect.")

def show_inventory():
    if player_state["inventory"]:
        print("You have:")
        for item in player_state["inventory"]:
            print(f"- {item.replace('_', ' ')}")
    else:
        print("You have no items.")


def examine(command=None):
    location = player_state["location"]
    room = rooms[location]

    # If no specific item is given, describe the room
    if not command or command.strip() == "":
        print(f"\n{room['description']}")

        items_in_room = room.get("items", [])
        reward_item = room.get("reward_item")

        if items_in_room:
            print("Items in room:")
            for item in items_in_room:
                print(f"- {item.replace('_', ' ')}")
        elif reward_item:
            print("Items in room:")
            print("- unknown")

        return

    item_key = command.replace(" ", "_").lower()

    if item_key not in player_state["inventory"]:
        print("You don't have that item.")
        return

    item_data = items.get(item_key, {})

    print(f"\n{item_data.get('description')}")

    # Handle interaction_on_examine if it exists
    interaction = item_data.get("interaction_on_examine")
    if interaction:
        prompt = interaction.get("prompt")
        outcomes = interaction.get("outcomes", {})

        if not outcomes:
            # If there are no outcomes, just display the prompt
            print(f"\n{prompt}")
            return

        valid_choices = list(outcomes.keys())

        while True:
            choice = input(f"\n{prompt} ").strip().lower()
            if choice in valid_choices:
                outcome = outcomes.get(choice)
                if outcome:
                    print(f"\n{outcome.get('prompt', '')}")
                    effects = outcome.get("effects", {})
                    for effect, value in effects.items():
                        if isinstance(value, bool):
                            player_state["event_flags"][effect] = value
                        if effect == "remove_from_inventory" and value:
                            if item_key in player_state["inventory"]:
                                player_state["inventory"].remove(item_key)
                break
            else:
                print(f"Please enter one of the following: {', '.join(valid_choices)}")


def take_item(item):
    # Normalize the item name: convert spaces (any count) into a single underscore
    item = "_".join(item.strip().split())

    location = player_state["location"]
    room = rooms[location]

    if item in room.get("items", []):
        player_state["inventory"].append(item)
        room["items"].remove(item)
        print(f"You take the {item.replace('_', ' ')}.")

        # If the item has an 'upon_take' message in the items dict, show it
        if item in items and "upon_take" in items[item]:
            print(f"\n{items[item]['upon_take']}")
    else:
        print("There is no such item here.")


def show_map(current_location):
    def mark(name):
        return f"[{name}]<--" if name == current_location else f"[{name}]"

    print("                         " + mark("mountain_peak"))
    print("                                 |")
    print("     " + mark("whispering_cave") + "   " + mark("echoing_ledge"))
    print("                 \\       /")
    print("               " + mark("deep_cave"))
    print("                   |")
    print("     " + mark("glowing_cave") + "  " + mark("shrouded_path"))
    print("                 \\       /")
    print("              " + mark("forest_entry"))



def main_game_loop():
    print_intro()
    print("Type 'help' to see controls.")
    while True:
        cmd = input("\n> ").strip().lower()

        if cmd in ["left", "right", "forward", "behind", "respawn"]:
            move_player(cmd)
        elif cmd == "examine":
            examine()  # No argument = show room description
        elif cmd.startswith("examine "):
            _, item = cmd.split(" ", 1)
            examine(item) #with argument = show item description
        elif cmd.startswith("take "):
            _, item = cmd.split(" ", 1)
            take_item(item)
        elif cmd == "inventory":
            show_inventory()
        elif cmd.startswith("use "):
            _, item = cmd.split(" ", 1)
            use_item(item)
        elif cmd == "save":
            save_game()
        elif cmd == "load":
            load_game()
            examine()
        elif cmd == "help":
            print_help()
        elif cmd == "map":
            show_map(player_state["location"])
        elif cmd == "quit":
            print("Goodbye.")
            break
        else:
            print("I don't understand that command. Type 'help' for options.")


if __name__ == "__main__":
    main_game_loop()

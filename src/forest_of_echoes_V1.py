from typing import Dict, List, Tuple

# Data structures define the story and options declaratively

Checkpoint = Dict[str, object]

CHECKPOINTS: List[Checkpoint] = [
    {
        "id": 1,
        "text": (
            "Checkpoint 1: Entering the Forest\nbitch"
            "As you stand at the threshold of the Forest of Echoes, the thick mist coils at your feet. "
            "The trees whisper tales of lost souls. Will you tread carefully or rush in boldly?\n"
            "🟢 Good/Cautious ➔ Path A\n🔴 Reckless ➔ Path B\n\n"
            "Path Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}"
        ),
        "options": [
            ("Tread quietly", "Good"),
            ("Charge through", "Reckless")
        ]
    },
    {
        "id": 2,
        "text": (
            "Checkpoint 2: Whispering Trees\n"
            "Deeper within, the forest seems to speak. Some voices sound warning, others tempting. "
            "Do you stop to listen or push forward ignoring the sounds?\n"
            "🟡 Curious/Explorer ➔ Path C\n🔴 Reckless ➔ Path B\n\n"
            "Path Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}"
        ),
        "options": [
            ("Listen to the whispers", "Explorer"),
            ("Ignore and keep walking", "Reckless")
        ]
    },
    {
        "id": 3,
        "text": (
            "Checkpoint 3: Wounded Traveler\n"
            "You find a wounded traveler slumped against a tree. They whisper of a powerful relic. "
            "Will you help them or leave them to their fate?\n"
            "🟢 Good/Cautious ➔ Path A\n🔴 Reckless ➔ Path B\n\n"
            "Path Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}"
        ),
        "options": [
            ("Help them", "Good"),
            ("Leave them", "Reckless")
        ]
    },
    {
        "id": 4,
        "text": (
            "Checkpoint 4: Glowing Cave or Shadowy Path\n"
            "The path splits—one side glows with a strange blue light from a nearby cave; the other is a shadowy trail "
            "through thick underbrush. Which will you explore?\n"
            "🟡 Curious/Explorer ➔ Path C\n🟢 Good/Cautious ➔ Path A\n\n"
            "Path Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}"
        ),
        "options": [
            ("Explore the glowing cave", "Explorer"),
            ("Take the shadow path", "Good")
        ]
    }
]

FINAL_CHECKPOINT: Checkpoint = {
    "id": 5,
    "text": (
        "Checkpoint 5: The Final Guardian\n"
        "You reach the edge of the forest. A massive beast stands guard over a golden altar. The Heart of Yurei gleams atop it. "
        "Will you fight, run, or attempt a trick?\n"
        "🟣 Secret/Unlockable ➔ Path D\n\n"
        "Path Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}"
    ),
    "options": [
        ("Fight with relic", "C"),
        ("Run away with relic", "A")
    ]
}

ENDINGS = {
    "A": "Ending A: Kai dies, you escape the forest, but the treasure is lost.",
    "B": "Ending B: You and Kai are killed by the guardian beast.",
    "C": "Ending C: You and Kai defeat the beast and claim the Heart of Yurei!"
}

# Pure functions handling logic

def update_path(path: Dict[str, int], trait: str) -> Dict[str, int]:
    new_path = path.copy()
    if trait in new_path:
        new_path[trait] += 1
    return new_path

def display_text(cp: Checkpoint, path: Dict[str, int], secret_path: bool) -> str:
    return cp["text"].format(
        Good=path.get("Good", 0),
        Reckless=path.get("Reckless", 0),
        Explorer=path.get("Explorer", 0),
        Secret=int(secret_path)
    )

def get_next_state(path: Dict[str, int], secret_path: bool, checkpoint_index: int, choice_index: int) -> Tuple[Dict[str, int], bool]:
    cp = CHECKPOINTS[checkpoint_index]
    trait = cp["options"][choice_index][1]
    new_path = update_path(path, trait)
    new_secret = secret_path or (checkpoint_index == 2 and trait == "Good")
    return new_path, new_secret

def determine_ending(path: Dict[str, int], secret_path: bool) -> str:
    if secret_path:
        return "SECRET"
    if path["Good"] >= 2:
        return "A"
    if path["Reckless"] >= 2:
        return "B"
    if path["Explorer"] >= 2:
        return "C"
    return "B"

# Input/output separated from logic

def prompt_choice(options: List[Tuple[str, str]]) -> int:
    for idx, (label, _) in enumerate(options, 1):
        print(f"{idx}. {label}")
    while True:
        try:
            choice = int(input("Choose 1 or 2: "))
            if choice in [1, 2]:
                return choice - 1
        except:
            pass
        print("Invalid choice. Please try again.")

def intro():
    print("""
Welcome to the Forest of Echoes.

You are Alex, a seasoned scavenger seeking the legendary treasure known as the Heart of Yurei.
Beside you is Kai, your fellow explorer, both determined to reach the peak of the elusive Mount Duskveil.

To get there, however, you must survive the Forest of Echoes—a place of ancient secrets, mythical beasts,
and paths that twist reality.

Each decision will shape your destiny. Choose wisely.
""")

def play_game():
    intro()
    path = {"Good": 0, "Reckless": 0, "Explorer": 0}
    secret_path = False

    for i, cp in enumerate(CHECKPOINTS):
        print("\n" + display_text(cp, path, secret_path))
        choice = prompt_choice(cp["options"])
        path, secret_path = get_next_state(path, secret_path, i, choice)

    print("\n" + display_text(FINAL_CHECKPOINT, path, secret_path))
    if secret_path:
        print("You use the relic from the traveler to unlock a secret path.")
        choice = prompt_choice(FINAL_CHECKPOINT["options"])
        ending_key = FINAL_CHECKPOINT["options"][choice][1]
    else:
        ending_key = determine_ending(path, secret_path)

    print("\n--- GAME END ---")
    print(ENDINGS[ending_key])

if __name__ == "__main__":
    play_game()

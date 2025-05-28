# Forest of Echoes: Python Text-Based Adventure (Declarative Style)

from functools import partial

# Define checkpoint data declaratively
checkpoints = [
    {
        "id": 1,
        "text": "Checkpoint 1: Entering the Forest\nAs you stand at the threshold of the Forest of Echoes, the thick mist coils at your feet. The trees whisper tales of lost souls. Will you tread carefully or rush in boldly?\n🟢 Good/Cautious ➔ Path A\n🔴 Reckless ➔ Path B\n\nPath Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}",
        "options": [
            ("Tread quietly", "Good"),
            ("Charge through", "Reckless")
        ]
    },
    {
        "id": 2,
        "text": "Checkpoint 2: Whispering Trees\nDeeper within, the forest seems to speak. Some voices sound warning, others tempting. Do you stop to listen or push forward ignoring the sounds?\n🟡 Curious/Explorer ➔ Path C\n🔴 Reckless ➔ Path B\n\nPath Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}",
        "options": [
            ("Listen to the whispers", "Explorer"),
            ("Ignore and keep walking", "Reckless")
        ]
    },
    {
        "id": 3,
        "text": "Checkpoint 3: Wounded Traveler\nYou find a wounded traveler slumped against a tree. They whisper of a powerful relic. Will you help them or leave them to their fate?\n🟢 Good/Cautious ➔ Path A\n🔴 Reckless ➔ Path B\n\nPath Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}",
        "options": [
            ("Help them", "Good"),
            ("Leave them", "Reckless")
        ]
    },
    {
        "id": 4,
        "text": "Checkpoint 4: Glowing Cave or Shadowy Path\nThe path splits—one side glows with a strange blue light from a nearby cave; the other is a shadowy trail through thick underbrush. Which will you explore?\n🟡 Curious/Explorer ➔ Path C\n🟢 Good/Cautious ➔ Path A\n\nPath Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}",
        "options": [
            ("Explore the glowing cave", "Explorer"),
            ("Take the shadow path", "Good")
        ]
    }
]

final_checkpoint = {
    "id": 5,
    "text": "Checkpoint 5: The Final Guardian\nYou reach the edge of the forest. A massive beast stands guard over a golden altar. The Heart of Yurei gleams atop it. Will you fight, run, or attempt a trick?\n🟣 Secret/Unlockable ➔ Path D\n\nPath Meter: Good: {Good}, Reckless: {Reckless}, Explorer: {Explorer}, Secret: {Secret}",
    "options": [
        ("Fight with relic", "C"),
        ("Run away with relic", "A")
    ]
}

endings = {
    "A": "Ending A: Kai dies, you escape the forest, but the treasure is lost.",
    "B": "Ending B: You and Kai are killed by the guardian beast.",
    "C": "Ending C: You and Kai defeat the beast and claim the Heart of Yurei!"
}

# Introduction
intro_text = """
Welcome to the Forest of Echoes.

You are Alex, a seasoned scavenger seeking the legendary treasure known as the Heart of Yurei.
Beside you is Kai, your fellow explorer, both determined to reach the peak of the elusive Mount Duskveil.

To get there, however, you must survive the Forest of Echoes—a place of ancient secrets, mythical beasts,
and paths that twist reality.

Each decision will shape your destiny. Choose wisely.
"""

def print_intro():
    print(intro_text)

def display_checkpoint(cp, path, secret_path):
    text_with_meter = cp["text"].format(
        Good=path["Good"], Reckless=path["Reckless"],
        Explorer=path["Explorer"], Secret=int(secret_path)
    )
    print(f"\n{text_with_meter}")
    for idx, (label, _) in enumerate(cp["options"], 1):
        print(f"{idx}. {label}")

def get_choice():
    while True:
        try:
            choice = int(input("Choose 1 or 2: "))
            if choice in [1, 2]:
                return choice
        except Exception:
            pass
        print("Invalid choice. Please try again.")

def play_game():
    path = {"Good": 0, "Reckless": 0, "Explorer": 0}
    secret_path = False

    print_intro()

    for i, cp in enumerate(checkpoints):
        display_checkpoint(cp, path, secret_path)
        choice = get_choice()
        selected_trait = cp["options"][choice - 1][1]
        path[selected_trait] += 1
        if i == 2 and selected_trait == "Good":
            secret_path = True

    display_checkpoint(final_checkpoint, path, secret_path)

    # Secret path logic
    if secret_path:
        print("You use the relic from the traveler to unlock a secret path.")
        for idx, (label, _) in enumerate(final_checkpoint['options'], 1):
            print(f"{idx}. {label}")
        ending = final_checkpoint['options'][get_choice() - 1][1]
    else:
        if path['Good'] >= 2:
            ending = "A"
        elif path['Reckless'] >= 2:
            ending = "B"
        elif path['Explorer'] >= 2:
            ending = "C"
        else:
            ending = "B"

    print("\n--- GAME END ---")
    print(endings[ending])

if __name__ == "__main__":
    play_game()

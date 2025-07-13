# Title: P5HW Instructions - Adventure Game
# Your Name: MathisMclean, Bernadette
# Date: 7/13/2025
# Assignment Name: P5HW Instructions - Adventure Game
# Brief description of program: This assignment is a Python program that allows you to get creative and design a game of your choosing. The game should take the user 5 minutes or less to complete. 



🏴‍☠️ Game Title: Treasure Hunt
Game Concept
The player must collect three special treasure items hidden across different locations—a jungle, a cave, and a beach. At each location, they solve a challenge (like a riddle or mini game) to earn an item. If they collect all three, they win!

Module Imports
python
import random
import time


👤 Value-Returning Function
python
def create_player(name):
    return {
        "name": name,
        "inventory": [],
        "score": 0
    }


Returns a dictionary that stores player info.
🧠 Game Logic Functions
python
def explore_location(location):
    print(f"\n🌍 You're exploring the {location}...")
    time.sleep(1)
    if location == "jungle":
        return "🍌 Golden Banana"
    elif location == "cave":
        return "💎 Sapphire Gem"
    elif location == "beach":
        return "🦴 Ancient Shell"

def solve_riddle():
    print("🧠 Solve this: What has a heart that doesn’t beat?")
    answer = input("Your answer: ").lower()
    if answer == "artichoke":
        print("✅ Correct!")
        return True
    else:
        print("❌ Incorrect!")
        return False


🔁 Loop (no while True)
python
locations = ["jungle", "cave", "beach"]
for place in locations:
    item = explore_location(place)
    if solve_riddle():
        player["inventory"].append(item)
        player["score"] += 10
    else:
        print("You missed the treasure here.")


🧾 If/Else Block
python
if len(player["inventory"]) == 3:
    print("🏆 You collected all treasures! You win!")
else:
    print("😢 You didn’t collect all treasures. Better luck next time.")


🚀 Main Function
python
def main():
    name = input("Enter your name, adventurer: ")
    global player
    player = create_player(name)
    print(f"\nWelcome {player['name']}! Let’s begin the Treasure Hunt!")

    for place in ["jungle", "cave", "beach"]:
        item = explore_location(place)
        if solve_riddle():
            print(f"You found {item}!")
            player["inventory"].append(item)
            player["score"] += 10
        else:
            print("No treasure here this time.")

    if len(player["inventory"]) == 3:
        print("🎉 Victory! You are the master treasure hunter!")
    else:
        print("Game over. Try again!")

main()


🎭 Character Backstory
Let players choose their adventurer type:
python
def select_role():
    print("Choose your role:")
    print("1. 🧭 Explorer")
    print("2. 🧙 Sorcerer")
    print("3. 🏹 Archer")
    choice = input("Enter 1, 2, or 3: ")
    roles = {"1": "Explorer", "2": "Sorcerer", "3": "Archer"}
    return roles.get(choice, "Explorer")


Include this in create_player() as an attribute!
🏔️ Environmental Hazards
Throw in surprise events:
python
def hazard_event():
    events = [
        "A wild monkey snatches a treasure! 🐒",
        "You slip on moss and lose 5 points 💦",
        "A magic portal teleports you forward! ✨"
    ]
    outcome = random.choice(events)
    print(outcome)


Call this randomly after each challenge to spice things up.
💡 Hint System (Optional Help)
If a riddle is missed, offer a hint:
python
def offer_hint():
    print("Would you like a hint? 🤔")
    hint = input("Type 'yes' or 'no': ").lower()
    if hint == "yes":
        print("Hint: It's something you eat that's green and layered.")


🎁 Secret Bonus Round
Unlockable if all treasures are collected:
python
def bonus_round():
    print("\n🎉 BONUS ROUND UNLOCKED!")
    print("Final riddle: I’m tall when I’m young and short when I’m old. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "candle":
        print("🔥 Correct! You win the ultra treasure: 🏆 Crown of Light!")
    else:
        print("Almost! But the treasure slips away...")
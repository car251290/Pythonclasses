import random

# 1. Create pairs of matching cards
cards = [
    "🍎", "🍎",
    "🐶", "🐶",
    "⚽", "⚽",
    "🚀", "🚀",
    "🎮", "🎮",
    "⭐", "⭐"
]

# 2. Shuffle the cards
random.shuffle(cards)

# 3. Create hidden cards
hidden_cards = ["?"] * len(cards)

# 4. Game variables global variables
matches = 0
attempts = 0

print("================================")
print("     MEMORY CARD CHALLENGE")
print("================================")
print("Find all the matching pairs!")
print("Choose two card positions from 1 to", len(cards))


# 5. Display the cards
def show_cards():
    print()

    for i in range(len(cards)):
        print(hidden_cards[i], end="  ")

        if (i + 1) % 4 == 0:
            print()

    print()


# 6. Play the game
while matches < len(cards) // 2:

    show_cards()

    # Choose the first card
    first = int(input("Choose the first card: ")) - 1

    if first < 0 or first >= len(cards):
        print("Invalid position! Try again.")
        continue

    if hidden_cards[first] != "?":
        print("That card is already matched!")
        continue

    # Reveal the first card
    hidden_cards[first] = cards[first]
    show_cards()

    # Choose the second card
    second = int(input("Choose the second card: ")) - 1

    if second < 0 or second >= len(cards):
        print("Invalid position! Try again.")
        hidden_cards[first] = "?"
        continue

    if second == first or hidden_cards[second] != "?":
        print("Choose a different hidden card!")
        hidden_cards[first] = "?"
        continue

    # Reveal the second card
    hidden_cards[second] = cards[second]
    show_cards()

    attempts += 1

    # 7. Check for a match
    if cards[first] == cards[second]:
        print("Great! You found a matching pair!")
        matches += 1
    else:
        print("Not a match! Try to remember the cards.")

        hidden_cards[first] = "?"
        hidden_cards[second] = "?"

    input("Press Enter to continue...")

# 8. Show the final score
print("\n================================")
print("          YOU WIN!")
print("================================")
print("Matching pairs:", matches)
print("Attempts:", attempts)
print("================================")
import random

# 1. CREATE PAIRS OF MATCHING CARDS
cards = [
    "🍎", "🍎",
    "🐶", "🐶",
    "⚽", "⚽",
    "🚀", "🚀",
    "🎮", "🎮",
    "⭐", "⭐"
]

# RANDOMIZE THE CARDS
random.shuffle(cards)

hidden_card = ["?"] * len(cards)

# 2. GLOBAL VARIABLES
matches = 0
attempts = 0

player_score = 0
computer_score = 0

# 3. AI MEMORY
computer_memory = {}

# 4. DISPLAY THE GAME
print("================================")
print("     MEMORY CARD CHALLENGE")
print("================================")
print("       PLAYER VS COMPUTER")
print("Find all the matching pairs!")
print("Choose two card positions from 1 to", len(cards))


# 5. DISPLAY CARDS FUNCTION
def show_cards():
    print("\n------------------------")

    for item in range(len(cards)):
        print(f"{item + 1}: {hidden_card[item]}", end="   ")

        if (item + 1) % 4 == 0:
            print()

    print("------------------------")


# 6. COMPUTER MEMORY FUNCTION
def remember_card(position):
    emoji = cards[position]

    if emoji not in computer_memory:
        computer_memory[emoji] = []

    if position not in computer_memory[emoji]:
        computer_memory[emoji].append(position)


# 7. COMPUTER FIRST CARD
def computer_first_card():

    # Search for a matching pair in memory
    for emoji in computer_memory:

        available = [
            p for p in computer_memory[emoji]
            if hidden_card[p] == "?"
        ]

        if len(available) >= 2:
            return available[0]

    # Choose a random hidden card
    unknown = [
        i for i in range(len(cards))
        if hidden_card[i] == "?"
    ]

    return random.choice(unknown)


# 8. COMPUTER SECOND CARD
def computer_second_card(first):

    emoji = cards[first]

    # Check if the computer remembers the matching card
    known_match = [
        p for p in computer_memory.get(emoji, [])
        if p != first and hidden_card[p] == "?"
    ]

    if known_match:
        return known_match[0]

    # Otherwise choose another random hidden card
    unknown = [
        i for i in range(len(cards))
        if hidden_card[i] == "?" and i != first
    ]

    return random.choice(unknown)


# 9. MAIN GAME LOOP
while matches < len(cards) // 2:

    # =================================
    # PLAYER TURN
    # =================================

    print("\n========== YOUR TURN ==========")
    show_cards()

    # FIRST CARD
    first = int(input("Choose your first card: ")) - 1

    if first < 0 or first >= len(cards):
        print("Invalid position! Try again.")
        continue

    if hidden_card[first] != "?":
        print("Invalid position! Try again.")
        continue

    hidden_card[first] = cards[first]
    show_cards()

    # SECOND CARD
    second = int(input("Choose your second card: ")) - 1

    if second < 0 or second >= len(cards):
        print("Invalid position! Try again.")
        hidden_card[first] = "?"
        continue

    if second == first or hidden_card[second] != "?":
        print("Choose a different card!")
        hidden_card[first] = "?"
        continue

    hidden_card[second] = cards[second]
    show_cards()

    attempts += 1

    # REMEMBER PLAYER REVEALED CARDS
    remember_card(first)
    remember_card(second)

    # CHECK PLAYER MATCH
    if cards[first] == cards[second]:

        print("Great! You found a matching pair!")

        matches += 1
        player_score += 1

    else:

        print("No match! Try to remember the cards.")

        hidden_card[first] = "?"
        hidden_card[second] = "?"

    input("Press ENTER to continue...")

    if matches == len(cards) // 2:
        break

    # =================================
    # COMPUTER TURN
    # =================================

    print("\n========== COMPUTER TURN ==========")

    # COMPUTER FIRST CARD
    ai_first = computer_first_card()

    hidden_card[ai_first] = cards[ai_first]

    print("Computer chooses its first card...")
    show_cards()

    # COMPUTER SECOND CARD
    ai_second = computer_second_card(ai_first)

    hidden_card[ai_second] = cards[ai_second]

    print("Computer chooses its second card...")
    show_cards()

    attempts += 1

    # COMPUTER REMEMBERS ITS CARDS
    remember_card(ai_first)
    remember_card(ai_second)

    # CHECK COMPUTER MATCH
    if cards[ai_first] == cards[ai_second]:

        print("The computer found a matching pair!")

        matches += 1
        computer_score += 1

    else:

        print("The computer did not find a match!")

        hidden_card[ai_first] = "?"
        hidden_card[ai_second] = "?"

    input("Press ENTER to continue...")


# 10. FINAL SCORE
print("\n================================")
print("             GAME OVER!")
print("================================")

show_cards()

print("Player score:", player_score)
print("Computer score:", computer_score)
print("Total attempts:", attempts)

if player_score > computer_score:

    print("CONGRATULATIONS! YOU WIN!")

elif computer_score > player_score:

    print("THE COMPUTER WINS!")

else:

    print("IT'S A TIE!")

print("================================")
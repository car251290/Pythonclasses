import random
import webbrowser

all_questions = [
    {
        "question": "Which country won the 2022 FIFA World Cup?",
        "answer": "argentina"
    },
    {
        "question": "Which country has won the most FIFA World Cups?",
        "answer": "brazil"
    },
    {
        "question": "How often is the FIFA World Cup held?",
        "answer": "every four years"
    },
    {
        "question": "Where was the first FIFA World Cup played?",
        "answer": "uruguay"
    },
    {
        "question": "In what year was the first FIFA World Cup held?",
        "answer": "1930"
    },
    {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": "au"
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "answer": "william shakespeare"
    }
]

# 2. Store websites
websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "python": "https://www.python.org",
    "scratch": "https://scratch.mit.edu",
    "world cup": "https://www.fifa.com"
}

# 3. Open a website
def open_website(user_input):
    user_input = user_input.lower().strip()

    for website in websites:
        if website in user_input:
            webbrowser.open(websites[website])
            return "Opening " + website + "..."

    return "Sorry, I don't know that website."


# 4. Ask a random question
def get_random_question():
    selected_question = random.choice(all_questions)
    return selected_question


# 5. Check the user's answer
def check_answer(user_answer, correct_answer):
    user_answer = user_answer.lower().strip()
    correct_answer = correct_answer.lower().strip()

    return user_answer == correct_answer


# 6. Play the quiz
def play_quiz():
    score = 0

    print("\nWelcome to Trivia Master!")
    print("Let's test your knowledge!")

    number_of_questions = len(all_questions)

    while True:
        try:
            number = int(input(
                "\nHow many questions would you like to answer? "
            ))

            if 1 <= number <= number_of_questions:
                break

            print("Please choose a number from 1 to", number_of_questions)

        except ValueError:
            print("Please enter a valid number.")

    # Select questions without repeating them
    selected_questions = random.sample(all_questions, number)

    # Ask each question
    for question_number, item in enumerate(selected_questions, start=1):
        print("\nQuestion", question_number)
        print(item["question"])

        user_answer = input("Your answer: ")

        if check_answer(user_answer, item["answer"]):
            print("Correct! Great job!")
            score += 1
        else:
            print("Not quite!")
            print("The correct answer is:", item["answer"])

    # Show the final results
    print("\n--- QUIZ RESULTS ---")
    print("Your score:", score, "out of", number)

    percentage = (score / number) * 100
    print("Your percentage:", round(percentage), "%")

    if percentage == 100:
        print("Excellent! Perfect score!")
    elif percentage >= 70:
        print("Great job! Keep practicing!")
    else:
        print("Keep learning! You can do better next time!")


# 7. Start the program
play_quiz()
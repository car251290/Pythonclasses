import random

# Dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "Feeling digital today!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["I'm not sure I understand.", "Could you say that again?"]
}
jokes = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
    "Debugging is like being a detective in a crime movie where you're also the murderer.",
    "Why did the programmer quit his job? Because he didn't get arrays."
]


# make facts of the world cup 
# variables 
world_cup_facts = [
    "The FIFA World Cup was first held in 1930.",
    "Brazil has won the most World Cups, with a total of 5 titles.",
    "The tournament is held every four years, with the next one scheduled for 2022 in Qatar.",
    "Germany and Italy have each won the World Cup 4 times.",
    "The 1994 World Cup in the USA was the first to be held in North America."
]
## math 
math = [
    "What is 2 + 2? 4",
    "What is the square root of 16? 4",
    "What is 5 * 6? 30",
    "What is 10 / 2? 5"
    
]

# All chatbot questions
all_questions = [
    # World Cup Questions
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

    # General Knowledge Questions
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
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "answer": "william shakespeare"
    }
]

# variables that remember the current question and answer
# the none help the computer to know that is not any current question or answer
current_question = None
current_answer = None

# function 
def get_anwer_to_question(question):
    for i in all_questions:
        if i["question"].lower() == question.lower():
            return i["answer"]
    return "I don't know the answer to that question."

#def ask_response_question():
 #   global questions
  #  current_question = random.choice(questions)
   # return current_question["question"], current_question["answer"]

def ask_response_question():
    selected_question = random.choice(all_questions)
    return selected_question["question"], selected_question["answer"]

# function to return the random question 
def get_random_question_all():
    return random.choice(all_questions)["question"]
    

# function of the world cup facts
def get_random_world_cup_facts():
    return random.choice(world_cup_facts)

def get_random_jokes():
    return random.choice(jokes)

def get_random_math():
    return random.choice(math)



# Function to get a response
def get_response(user_input):
    global current_question, current_answer
    # make the if statement for all the questions in the questions list
    if "all questions" in user_input:
        return get_random_question_all()
    
    if "question" in user_input:
        current_question, current_answer = ask_response_question()
        return current_question
    
    if "math" in user_input:
        return get_random_math()
    
    if "questions" in user_input:
        return ask_response_question()[0]
    if user_input == "ask me a question":
        current_question, current_answer = ask_response_question()
        return current_question
    if "answer" in user_input:
        if current_answer:
            return f"The answer is: {current_answer}"
        else:
            return "I haven't asked a question yet. Please ask a question first."
        
    if "answer" in user_input:
        if current_answer:
            return f"The answer is: {current_answer}"
        else:
            return "I haven't asked a question yet. Please ask a question first."   
        
    #check the user user's input and respond accordingly
    if current_question and current_answer:
        if user_input.lower() == current_answer.lower():
            response = "Correct! Well done."
            current_question, current_answer = None, None  # Reset after correct answer
            return response
        else:
            return "That's not correct. Try again or ask for the answer."
        

    #variables
    user_input = user_input.lower()
    #if "jokes" in user_input:
     #   return get_random_jokes()
    #foorloops
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
        if "jokes" in user_input:
            return get_random_jokes()
        # create a if statement where you can display the facts random way
        if "facts" in user_input:
            return get_random_world_cup_facts()
        if "math" in user_input:
            return random.choice(math)

    return random.choice(responses["default"])

# Chat loop
print("AI Chatbot (type 'quit' to exit)")
while True:
    user_text = input("You: ")
    if user_text.lower() == "quit":
        print("Chatbot: Bye!")
        break
    reply = get_response(user_text)
    print("Chatbot:", reply)

import random

# Dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "Feeling digital today!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["I'm not sure I understand.", "Could you say that again?"]
}

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Chat loop
print("🤖 AI Chatbot (type 'quit' to exit)")
while True:
    user_text = input("You: ")
    if user_text.lower() == "quit":
        print("Chatbot: Bye! 👋")
        break
    reply = get_response(user_text)
    print("Chatbot:", reply)
def ask_questions(name):
    print(f"Hello, {name}!")
    question1 = "What is your favorite color? "
    answer1 = input(question1)
    question2 = "What is your favorite food? "
    answer2 = input(question2)
    question3 = "What city do you live in? "
    answer3 = input(question3)
    print(f"Your favorite color is {answer1}.")
    print(f"Your favorite food is {answer2}.")
    print(f"You live in {answer3}.")
    # Ask for X or O and respond accordingly
    #if statement how will be used 
    XO = input("Choose X  OR O: ").strip().upper()

    if XO == "X":
        print("You wrote X!")
    elif XO == "O":
        print("You wrote O!")
    else:
        print("Invalid choice. Please choose X or O next time.")

name = "Javier"
ask_questions(name)
## this example will be for Tuesday 
def explain_for_loop():
    for i in range(5):
        print("Learning Python!")
    arr = ["apple", "banana", "cherry"]
    for i in arr :
        print(i)
explain_for_loop()


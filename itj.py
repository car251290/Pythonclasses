

def sum(a,b):
    return a+b
sum(1,2)


def statement():
    code = input("Enter a programming language: ")
    
    if code == "python":
        print ("Python is a programming language")
    if code  == "JS" :
        print ("JS is a programming language")
    if code == "Java":
            print ("Java is a programming language")
    else:
            print("I don't know that language")
statement()
## dictonary as a switch statement

def week_task(day):
    week = {
        'Monday': 'Go to work',
        'Tuesday': 'Go to the GYM',
        'Wednesday': 'Go to the library',
        'Thursday': 'Go to the park',
        'Friday': 'Go to the movies',
        'Saturday': 'Go to the beach',
        'Sunday': 'Go to church'
    }
    result = week.get(day, 'Invalid day')
    return result
day_option = input("Enter a day of the week: ")
result1 = week_task(day_option)

print(result1)


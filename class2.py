# Ask for age first
age = int(input("Enter your age: "))

# Ask for your name
name = input("Enter your name: ")

print("My name is " + name + " and I am " + str(age) + " years old.")

# Ask for 2 more names
for i in range(2):
    other_name = input("Enter another name: ")
    print(other_name + " is a great name!")

# Check if the person is adult or minor
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Final message
print("Nice to meet you " + name + ", age " + str(age) + ". Thanks for adding your information!")
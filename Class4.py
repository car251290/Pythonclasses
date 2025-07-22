class MyClass:
    def __init__(self, name, age):
        # Constructor to initialize the class attributes
        self.name = name
        self.age = age

    def greet(self):
        # Function to display a greeting message
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def increment_age(self):
        # Function to increment the age by 1
        self.age += 1
        return f"{self.name}'s age is now {self.age}."

# Example usage:
# obj = MyClass("Alice", 30)
# print(obj.greet())
# print(obj.increment_age())class MyClass:
    def __init__(self, name, age):
        # Constructor to initialize the class attributes
        self.name = name
        self.age = age

    def greet(self):
        # Extended function to display a detailed greeting message
        if self.age < 18:
            return f"Hello, my name is {self.name}. I am {self.age} years old, and I am a minor."
        elif self.age < 65:
            return f"Hello, my name is {self.name}. I am {self.age} years old, and I am an adult."
        else:
            return f"Hello, my name is {self.name}. I am {self.age} years old, and I am a senior citizen."

    def increment_age(self):
        # Extended function to increment the age by 1 and provide a detailed message
        self.age += 1
        if self.age < 18:
            return f"{self.name}'s age is now {self.age}. They are still a minor."
        elif self.age < 65:
            return f"{self.name}'s age is now {self.age}. They are an adult."
        else:
            return f"{self.name}'s age is now {self.age}. They are a senior citizen."

# Example usage:
# obj = MyClass("Alice", 30)
# print(obj.greet())
# print(obj.increment_age())
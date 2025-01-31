class Calculator:
    def __init__(self):
        print("Calculator is ready to use")
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

def main():
    calc = Calculator()
    operations = {
        '1':calc.add,
        '2':calc.sub,
        '3':calc.multiplication,
        '4':calc.division
        
    }
    while True:
        print('Select Operation')
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '5':
            break
        if choice in operations:
            a = int(input("Enter a number:"))
            b = int(input("Enter a number:"))
            result = operations[choice](a, b)
            print (f"Result:, {result}")
        else:
            print("Invalid Choice")
    
if __name__ == "__main__":
    main()
    
                    
                        




class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print(f"Name: {self.lastName}, {self.firstName}\nID: {self.idNumber}")


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores) / len(self.scores) if self.scores else 0
        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'

    def display_info(self):
        avg = sum(self.scores) / len(self.scores) if self.scores else 0
        return f"Name: {self.firstName} {self.lastName}, ID: {self.idNumber}, Average: {avg:.2f}, Grade: {self.calculate()}"


# Example usage and testing
if __name__ == "__main__":
    # Create a student instance
    student1 = Student("John", "Doe", 12345, [85, 90, 78, 92, 88])
    
    # Print student information
    student1.printPerson()
    print(f"Grade: {student1.calculate()}")
    print(student1.display_info())
    
    # Test different grade levels
    print("\n--- Testing different grade levels ---")
    
    # Outstanding student
    student2 = Student("Alice", "Smith", 12346, [95, 98, 92, 96, 94])
    print(f"Alice's grade: {student2.calculate()}")
    
    # Poor student
    student3 = Student("Bob", "Johnson", 12347, [45, 50, 48, 52, 46])
    print(f"Bob's grade: {student3.calculate()}")
    
    # Failing student
    student4 = Student("Charlie", "Brown", 12348, [30, 35, 25, 38, 32])
    print(f"Charlie's grade: {student4.calculate()}")
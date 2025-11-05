class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
        class Student(Person):
            def __init__(self, firstName, lastName, idNumber, scores):
                super().__init__(firstName, lastName, idNumber)
                self.scores = scores

            def calculate(self):
                avg = sum(self.scores) / len(self.scores) if self.scores else 0
                if avg >= 90:
                    return 'O'
                if avg >= 80:
                    return 'E'
                if avg >= 70:
                    return 'A'
                if avg >= 55:
                    return 'P'
                if avg >= 40:
                    return 'D'
                return 'T'
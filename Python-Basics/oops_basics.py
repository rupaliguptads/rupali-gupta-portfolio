# Object-Oriented Programming (OOP) Basics

# Example 1: Create a class and an object
class Student:
    def introduce(self):
        print("Hello! I am a student.")


student1 = Student()
student1.introduce()


# Example 2: Use attributes with a constructor
class StudentInfo:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")


student2 = StudentInfo("Rupali", "BTech CSE")
student2.display_info()


# Example 3: Add a method that returns a value
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()
print("Sum:", calculator.add(10, 20))
print("Product:", calculator.multiply(5, 4))


# Example 4: Create multiple objects
student3 = StudentInfo("Aman", "BTech CSE")
student4 = StudentInfo("Neha", "BSc Data Science")

student3.display_info()
student4.display_info()

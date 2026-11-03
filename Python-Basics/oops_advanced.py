# Advanced Object-Oriented Programming (OOP)

# Example 1: Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying Python.")


student = Student("Rupali")
student.introduce()
student.study()


# Example 2: Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rupali", 1000)
account.deposit(500)
print("Current balance:", account.get_balance())


# Example 3: Polymorphism
class Dog:
    def speak(self):
        print("Dog says: Woof!")


class Cat:
    def speak(self):
        print("Cat says: Meow!")


for animal in [Dog(), Cat()]:
    animal.speak()


# Example 4: Method overriding
class Animal:
    def sound(self):
        print("Animals make different sounds.")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo!")


cow = Cow()
cow.sound()

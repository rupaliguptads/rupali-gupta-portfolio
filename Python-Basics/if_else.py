# Check whether a student has passed

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# if-elif-else

# Example 1: Grade Calculator

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

# Example 2: Nested If

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")

    if marks >= 75:
        print("Distinction")
    else:
        print("Pass, but no distinction")
else:
    print("Fail")

# Multiple conditions usind and

# Example 3: Eligibility Check

age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

if age >= 18 and marks >= 60:
    print("Eligible")
else:
    print("Not eligible")

# Nested conditions

# Example 4: Find the Largest of Three Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Largest:", a)
    else:
        print("Largest:", c)
else:
    if b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)



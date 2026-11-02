# Marks Calculator

name = input("Enter your name: ")
marks = float(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks >= 40:
    print("Student Name:", name)
    print("Marks:", marks)
    print("Result: Pass")
else:
    print("Student Name:", name)
    print("Marks:", marks)
    print("Result: Fail")



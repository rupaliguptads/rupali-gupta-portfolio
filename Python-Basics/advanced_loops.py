# Advanced Python Loops

# Example 1: enumerate()
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# Example 2: zip()
names = ["Aman", "Rupali", "Neha"]
marks = [75, 90, 82]

for name, mark in zip(names, marks):
    print(f"{name}: {mark}")


# Example 3: Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Example 4: Loop with else
for number in range(1, 6):
    print(number)
else:
    print("Loop completed successfully.")


# Example 5: break
for number in range(1, 11):
    if number == 5:
        break
    print(number)


# Example 6: continue
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

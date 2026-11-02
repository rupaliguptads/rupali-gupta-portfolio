# Python Regular Expressions Examples

import re

# Example 1: Find numbers in text
text = "I studied for 4 hours and solved 25 questions."

numbers = re.findall(r"\d+", text)

print("Numbers found:", numbers)

# Example 2: Find all words starting with "P"
text = "Python is Powerful and Practical."

words = re.findall(r"\bP\w*", text)

print("Words starting with P:", words)


# Example 3: Check whether text starts with a pattern
text = "Python programming"

if re.match(r"Python", text):
    print("Text starts with Python")


# Example 4: Search for a word
text = "I am learning Python programming."

match = re.search(r"Python", text)

if match:
    print("Found:", match.group())
    print("Position:", match.start())


# Example 5: Replace text
text = "Python is easy. Python is useful."

updated_text = re.sub(r"Python", "Programming", text)

print("Updated text:", updated_text)


# Example 6: Validate an email format
email = "student@example.com"

pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Email format looks valid")
else:
    print("Invalid email format")


# Example 7: Extract dates
text = "Start date: 12-05-2026, End date: 20-06-2026"

dates = re.findall(r"\d{2}-\d{2}-\d{4}", text)

print("Dates found:", dates)


# Example 8: Remove extra spaces
text = "Python    is   very    useful"

cleaned_text = re.sub(r"\s+", " ", text).strip()

print("Cleaned text:", cleaned_text)

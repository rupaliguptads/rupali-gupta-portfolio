# Python String Handling Examples

# Example 1: Remove extra spaces
text = "   Python Programming   "

clean_text = text.strip()

print("Original text:", repr(text))
print("Cleaned text:", clean_text)


# Example 2: Count characters and words
sentence = "Python is useful for data analysis"

print("Total characters:", len(sentence))
print("Total words:", len(sentence.split()))


# Example 3: Count occurrences
message = "python is easy and python is powerful"

print("Occurrences of python:", message.count("python"))


# Example 4: Find and replace text
text = "I am learning Java"

print("Position of Java:", text.find("Java"))

updated_text = text.replace("Java", "Python")
print("Updated text:", updated_text)


# Example 5: Check string content
word = "Python123"

print("Alphanumeric:", word.isalnum())
print("Alphabetic:", word.isalpha())
print("Digits only:", word.isdigit())


# Example 6: Split a sentence into words
sentence = "I am learning Python"

words = sentence.split()

print("Words:", words)


# Example 7: Join words into a sentence
words = ["Python", "is", "interesting"]

sentence = " ".join(words)

print("Sentence:", sentence)


# Example 8: Reverse a string
text = "Python"

print("Reversed string:", text[::-1])


# Example 9: Check for a palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


print("madam:", is_palindrome("madam"))
print("hello:", is_palindrome("hello"))
print("nurses run:", is_palindrome("nurses run"))

# Python String Examples

# Example 1: Creating strings
name = "Rupali"
course = "Machine Learning"

print("Name:", name)
print("Course:", course)


# Example 2: String methods
text = "  python programming  "

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Without extra spaces:", text.strip())
print("Title case:", text.strip().title())


# Example 3: String length
message = "Hello, Python!"
print("Length:", len(message))


# Example 4: Accessing characters
word = "Python"

print("First character:", word[0])
print("Last character:", word[-1])


# Example 5: String slicing
print("First three characters:", word[:3])
print("Last three characters:", word[-3:])


# Example 6: Checking a substring
sentence = "I am learning Python"

print("Python present:", "Python" in sentence)


# Example 7: Replacing text
text = "I like Java"
updated_text = text.replace("Java", "Python")

print("Updated sentence:", updated_text)


# Example 8: Splitting and joining strings
languages = "Python,SQL,Excel"

language_list = languages.split(",")
print("Language list:", language_list)

joined_text = " | ".join(language_list)
print("Joined text:", joined_text)


# Example 9: f-strings
name = "Rupali"
skill = "Python"

print(f"{name} is learning {skill}.")

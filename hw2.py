paragraph = """
Python is a popular programming language.
This Python course teaches basic programming concepts,
variables, loops, functions, and data handling.
It is a beginner-friendly course for students.
"""

print("Length of paragraph:", len(paragraph))
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
print("Preview:", paragraph[:50])
paragraph = paragraph.replace("Python", "PYTHON")
print(paragraph)
paragraph = paragraph.lower()
paragraph = paragraph.strip()
words = paragraph.split()
print("Words:", words)
print(paragraph.count("course"))

print("The course description is {} characters long and has {} words.".format(
    len(paragraph), len(words)
))


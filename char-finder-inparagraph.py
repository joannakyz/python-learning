paragraph = "Python is a high-level, interpreted programming language known for its readability and simplicity. It supports multiple " \
"programming paradigms, including object-oriented, procedural, and functional programming. With a large standard library and countless " \
"third-party modules, Python is widely used in web development, data science, automation, artificial intelligence, and more. Its clean " \
"syntax allows developers to write fewer lines of code compared to other languages. Python's active community continually contributes to " \
"its growth, making it one of the most popular and beginner-friendly languages in the world."

print(paragraph)

paragraph_list = list(paragraph)

print(paragraph_list)

dictionary = {}

for char in paragraph_list:
    if char not in dictionary:
        dictionary[char] = 0
    else:
        dictionary[char] += 1

print(dictionary)

print("Number of 'i':", dictionary.get('i', 0))

print("max", max(list(dictionary.values())))
print("min", min(list(dictionary.values())))

for key, value in dictionary.items():
    if value == max(list(dictionary.values())):
        print(key, value)

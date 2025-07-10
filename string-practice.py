empty_string = ""
word_string = "Hello"
phrase_string = "I said Hi!"
multiple_strings = """
Hello there!
This is a second sentence. 
This is a third sentence.
"""

print("empty string: ", empty_string)
print("word: ", word_string)
print("multiple strings: ", multiple_strings)

name = "Ioanna"

print(name * 3) #prints name 3 times
print((name + " ") * 3) #prints name 3 times with a space in between
print(name[1]) #prints the second letter from the name string
print(name[1:4]) #prints the 2nd, 3rd and 4th letter from the string --> oan
print(name[-6: -1])
print(len(name)) #prints the length of the string
print(max(name.lower()))
print(min(name.lower()))

print(name.index("oa")) #searches if the string oa exists in the string name
print(name.count("a")) #returns the count of the letter

print("\"Hello World!\"")
print("\'Hello world!\'")
print("Hello /\\")
print("Ioanna return \r Maria")
print("Ioanna\bKyz") #removes a 
print("Hello world \t hi")
paragraph = "Hello world \t hello world"
paragraph = paragraph.expandtabs(15)
print(paragraph)


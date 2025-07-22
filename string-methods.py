#Methods for upper and lower - case letters

string = "The sun set behind the hills."
lower_string = "the sky was painted with soft pink clouds."
cap_string = "THE WIND BLEW THROUGH THE TREES."
rand_string = "ThE MoOnLiGhT dAnCeD oN tHe LaKe."

print(lower_string.capitalize()) #capitalizes only the first letter 
print(cap_string.lower()) #turns all letters lowercase
print(cap_string.casefold()) #more powerfull for "weird" languages
print(lower_string.upper()) #capitalizes all letters
print(lower_string.title()) #capitalizes first letters of each word 
print(rand_string.swapcase()) #turns cap into lower and the other way around

#Predicate Methods (methods for checking string case):

string1 = "Room42B is on the 3rd floor."
string2 = "the rain gently tapped on the window."
string3 = "BeautifulSunshine"
string4 = "BEAUTIFULSUNSHINE"
string5 = "42"
string6 = "Hello, World! 123 @#&$%"
string7 = "Hello\nWorld\t!"
string8 = "Joanna Kyz"
string9 = "19.4"
string10 = "1/2"
string11 = "       "

print(string1.isalnum()) #checks if string contains either numbers or letters or both (NOT SYMBOLS)
print("abc123".isalnum())
print(string3.isalpha()) #checks if string contains only letters 
print(string2.isalpha())
print(string5.isdigit()) #checks if string contains only numbers
print(string5.isdecimal()) #checks if string contains only decimal digits (0 - 9) not float (. or ,)
print(string9.isdecimal())
print(string10.isnumeric()) #checks if a string is numeric in other languages f.e. (not just digits)
print(string5.isspace()) #checks if a string is space only 
print(string11.isspace())
print(string6.isprintable()) #checks if a string contains only printable characters
print(string7.isprintable())
print("x 2".isidentifier()) #checks if the name of tha variable is valid or not
print("x_2y".isidentifier())
print(string2.islower()) #checks if the string contains only lowercase letters
print(string4.isupper()) #chekcs if the string contains only uppercase letters
print(string8.istitle()) #chekcs if in the string every first letter is capital

#space management and allignment

space_string = "   this sentence starts with spaces   "
print("1." + space_string.strip()) #removes spaces at beggining and end
print("2." + space_string.lstrip()) #removes spaces at the beggining
print("3." + space_string.rstrip()) #removes spaces at the end

paragraph = "      The morning air was cool and crisp. Birds chirped softly in the distance as sunlight filtered through the trees.     "

print(paragraph)
print("-------------------------------------")
print("|" + paragraph.strip().ljust(120) + "|") #left align and total width of 120 characters (if paragraph < 120 then the rest will be spaces at the end)
print("-------------------------------------")
print("|" + paragraph.strip().rjust(120)) #right align and total width of 120 characters (if paragraph < 120 then the rest will be spaces at the beggining)
print("-------------------------------------")
print("|" + paragraph.strip().center(120) + "|") #center align and total width of 120 characters (if paragraph < 120 then the rest will be spaces at the beggining and end)
print("-------------------------------------")

word = "word"
print(word.zfill(2)) #adds the remainder count of 0 at the beggining if the length of the string < 2
print(word.zfill(10)) #output: 000000word cuz length of word = 4, n = 10 -> 6 zeros remaining

#searching and replacing words or strings in paragraphs

sentence = "The cat sat on the mat."

print(sentence.startswith("The")) #returns T/F if the sentence starts with "The"
print(sentence.startswith("the"))
print(sentence.lower().startswith("the"))
print(sentence.startswith("cat",5)) #returns T/F if the sentence in position 5 starts with cat
print(sentence.startswith("cat",4,10)) #returns T/F if the sentence in range of position [4,10] has the word cat
print(sentence.endswith(".")) #returns T/F if the sentence ends with "."
print(sentence.endswith("mat",19,22))
print(sentence.find("cat")) #returns the position in which the word is found (not the range)
print(sentence.find("catt")) #returns -1 if not found
print("cat: ", sentence.index("cat")) #same as find but if not found then -> error
new_sentence = sentence.replace("cat", "kitten")
print("New sentence: ", new_sentence)

#finds how many times the word rain emerges
text = "The rain began to fall softly in the evening. As the rain picked up, people rushed to find shelter. Rain always reminded her of quiet days and warm tea."
text = text.lower()
pos = -1 #I want to start at position = 0 

lastpos = text.rfind("rain")

while pos != lastpos:
    pos = text.find("rain", pos + 1)
    print(pos, end = " ")

#replace word in sentence with its capital letters
saying = "I don't hate them.. I just feel better when they're not around."
saying_lower = saying.lower()

while True:
    user_input = input("insert word to replace: ")
    
    if user_input.isalpha():
        user_input.strip()
        user_input = user_input.lower()

        break
    else:
        print("only characters")

if user_input in saying_lower:
    saying = saying.replace(user_input, user_input.upper())
else:
    print("word does not exist.")

print(saying)

#splitting strings and paragraphs
sentence_2 = "You have to die a few times before you can really live."

print(sentence_2.split()) #removes spaces 
print(sentence_2.split("a")) #removes a's
print(sentence_2.split(" ", 2)) #creates a list with 3 items, first two words (2) and then the rest of the sentence
print(sentence_2.rsplit(" ", 2)) #does the same as above but starts spliting from the end
print(sentence_2.partition("few")) #creates a list with 3 items, 1st: left from word "few", 2nd: "few", 3rd: right from "few"
print(sentence_2.rpartition("r")) #creates a list with 3 items, 1st: left from letter "r", 2nd: "r", 3rd: right from "r"

paragraph_new = """
Some lose all mind and become soul, insane.
some lose all soul and become mind, intellectual.
some lose both and become accepted.
"""

print(paragraph_new)
print(paragraph_new.splitlines()) #creates a list with each line being an element

#program that finds a word in a text and replaces it with its capital letters
poem = """There's a bluebird in my heart that
wants to get out
but I'm too tough for him,
I say, 
stay down, do you want to mess me up?
you want to screw up the works?
you want to blow my book sales in Europe?
"""


while True: 
    word_input = input("Enter a word: ")
    word_input.split()

    if word_input.isalpha():
        word_input = word_input.lower()
        break
    else:
        print("Only characters please!")

poem_lowered = poem.lower()

poem_lines = poem_lowered.splitlines() #splits the paragraph into lines and saves them into a list
print(poem_lines)

for pos in range(len(poem_lines)):
    if poem_lines[pos].find(word_input) != -1:
        print("Line " + str(pos) + ":" + poem_lines[pos].replace(word_input, word_input.upper()))
        print(poem_lines[pos].replace(word_input, word_input.upper()))

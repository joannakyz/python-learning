words = "After the storm passed, the children ran outside, laughing, splashing in puddles, and chasing the rainbow across the sky."

letters = set(words)

print(letters) #prints only one time each letter from the string 

dictionary  = {letter: 0 for letter in letters }
print(dictionary)

for char in words:
    dictionary[char] += 1

print(dictionary)

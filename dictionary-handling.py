dictionary = {
    "name": "Ioanna", 
    "surname": "Kyzeridou",
    "age": 24,
    "degree": "Physics"
}

if "name" in dictionary:
    print("exists")
if "hobby" not in  dictionary:
    dictionary["hobby"] = "Gym"

print(dictionary)

print("~~~~~keys~~~~~")
for key in dictionary:
    print(key)

print("~~~~~keys and values~~~~~")
for key, value in dictionary.items():
    print(key, " : " ,value)

print("(~~~~~keys~~~~~")
for key in dictionary.keys():
    print(key)

print("~~~~~values~~~~~")
for value in dictionary.values():
    print(value)

print("~~~~~sorted keys~~~~~")
for key in sorted(dictionary.keys()):
    print(key)

print("~~~~~values~~~~~")
for key in set(dictionary.values()):
    print(key)

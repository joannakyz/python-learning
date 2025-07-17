name = input("Insert your first name: ")
surname = input("Insert your last name: ")

name = name.strip() 
surname = surname.strip()

while name.isalpha() is False or surname.isalpha() is False:
    if name.isalpha() is False:
        name = input("Insert your first name correctly: ")
        name = name.strip()
    elif surname.isalpha() is False:
        surname = input("Insert your last name correctly: ")
        surname = surname.strip()

if name.istitle() is False or surname.istitle() is False:
    name = name.title()
    surname = surname.title()


print("Full name: " ,name , " " , surname)

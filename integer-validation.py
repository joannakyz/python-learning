x = input("Give an integer: ")

while x.isdigit() is False:
    x = input("Give an integer again: ")

    if x.isdigit() is True:
        num = int(x)
        print(num)

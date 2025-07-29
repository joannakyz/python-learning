def input_integet():
    while True:
        data = input("Enter an int: ")
        if data.isdigit():
            return int(data)
        else:
            print("Only digits..")


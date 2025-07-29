def input_float():
    while True:
        data = input("Enter a float: ")
        data_1 = list(data)
        if "." in data_1:
            return float(data)
        else:
            print("Only float!")

      

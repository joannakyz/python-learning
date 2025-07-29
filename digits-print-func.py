def digits_print(number):
    third_digit = number % 10
    number = number // 10
    second_digit = number % 10
    first_digit = number // 10
    
    print(f"First digit: {first_digit}")
    print(f"Second digit: {second_digit}")
    print(f"Thrid digit: {third_digit}")



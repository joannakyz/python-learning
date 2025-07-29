def is_square(number):
    for i in range(2, number // 2 + 1):
        if i ** 2 == number:
            return True
    return False

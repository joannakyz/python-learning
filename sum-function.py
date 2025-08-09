def my_sum(*numbers):
    print(numbers)
    count = 0

    for number in numbers:
        count += number
    
    return count


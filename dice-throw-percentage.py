from random import seed
from random import randrange
from datetime import datetime

seed()

numbers = {}

for i in range(1, 6 + 1):    
    numbers[i] = 0

print(numbers)

for j in range(1000000):
    x = randrange(1, 6 + 1)
    numbers[x] += 1

print(numbers)


for i in range(1, 6 + 1):
    print("percentage: ", numbers[i] / 1000000 )

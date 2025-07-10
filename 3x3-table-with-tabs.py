from random import seed
from random import randrange
from datetime import datetime

seed()

array_3x3 = []

for row in range(3):
    new_row = []
    for item in range(3):
        new_row.append(randrange(0, 1000))
    array_3x3.append(new_row)

print(array_3x3)

for row in array_3x3:
    print("+-----" * 3 + "+", end="")
    print(" ")
    for item in row:
        print(("|" + str(item) + "\t").expandtabs(6), end="")
    print("|")
print("+-----" * 3 + "+", end="")

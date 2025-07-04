evens = set()
odds = set()
mul3 = set()
prime = set()
for i in range(0, 100 + 1):
    if i % 2 == 0:
        evens.add(i)
    else:
        odds.add(i)
    if i % 3 == 0:
        mul3.add(i)
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if i != 0 and i != 1:
            prime.add(i)
print("evens: ", evens)
print("odds: ", odds)
print("mul3: ", mul3)
print("prime: ", prime)

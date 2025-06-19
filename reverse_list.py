def reverselist(lista):
    lista.sort()
    b = lista[::-1]
    print("sorted: ", lista)
    print("reversed: ", b)
    
lista1 = []
a = int(input("Enter length: "))
for i in range(0, a):
    item = input("insert list: ")
    lista1.append(item)

print(lista1)
reverselist(lista1)

#asc

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

lista = [5, 24, 76, 3, 8, 45, 87, 2, 9, 10, 0, 15, 17]

print(lista)
insertion_sort(lista)
print(lista)

#desc

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] > array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

lista = [5, 24, 76, 3, 8, 45, 87, 2, 9, 10, 0, 15, 17]

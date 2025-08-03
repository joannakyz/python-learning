def binary_search(arr, num):
    arr.sort()
    start = 0
    end = len(arr) - 1
    print("sorted list: ", arr)
    while start <= end:
        position = (start + end) // 2
        if arr[position] == num:
            print("Found num: ", num, " in  Position: ", position)
            return
        elif arr[position] > num:
            end = position - 1
        else:
            start = position + 1

    print("Not found.")


def binary_search(a_list, element, start, end):
    a_list = sorted(a_list)  

    if start > end:
        return -1  

    pos = (start + end) // 2

    if element == a_list[pos]:
        return pos
    elif element < a_list[pos]:
        return binary_search(a_list, element, start, pos - 1)
    else:
        return binary_search(a_list, element, pos + 1, end)


def binary_search(arr, ele):
    arr_sort = sorted(arr)
    start = 0
    end = len(arr_sort) - 1

    while start <= end:
        pos = (start + end) // 2

        if arr_sort[pos] == ele:
            return pos + 1  
        elif arr_sort[pos] > ele:
            end = pos - 1
        else:
            start = pos + 1

    return -1  

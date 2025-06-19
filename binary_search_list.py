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

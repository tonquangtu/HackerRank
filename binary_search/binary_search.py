
def binary_search(arr, start, end, x):
    if start >= end:
        if arr[start] == x:
            return start
        else:
            return -1

    middle = int((start + end)/2)
    if x == arr[middle]:
        return middle

    elif x < arr[middle]:
        return binary_search(arr, start, middle - 1, x)
    else:
        return binary_search(arr, middle + 1, end, x)


# Test binary search

arr_test = [1, 3, 5, 6, 8, 12, 13, 13]
x = 5
result = binary_search(arr_test, 0, len(arr_test) - 1, x)
print('result', result)

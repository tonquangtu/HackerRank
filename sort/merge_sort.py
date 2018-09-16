

def sort(arr):
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)


def merge_sort(arr, start, end):
    if start >= end:
        return
    medium = int((start + end) / 2)
    merge_sort(arr, start, medium)
    merge_sort(arr, medium + 1, end)
    merge(arr, start, end, medium)


def merge(arr, start, end, medium):
    left_arr = arr[start:medium + 1]
    right_arr = arr[medium + 1:end + 1]

    l = 0
    r = 0
    index = start
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            arr[index] = left_arr[l]
            l += 1
        else:
            arr[index] = right_arr[r]
            r += 1
        index += 1

    while l < len(left_arr):
        arr[index] = left_arr[l]
        l += 1
        index += 1

    while r < len(right_arr):
        arr[index] = right_arr[r]
        r += 1
        index += 1


# Test
test_arr = [1, 2, 3, 5, 1, -5, 3, 5, -7, 9, 30, -14]
test_arr2 = [1]
sort(test_arr)
sort(test_arr2)
sort([])


# Way 1: Using divide and conquer.
def find_largest_sub_arr(arr):
    return find_max_sub(arr, 0, len(arr) - 1)


def find_max_sub(arr, start, end):
    if start >= end:
        return arr[start]

    medium = int((start + end) / 2)
    # Find largest sub array in left
    ml = find_max_sub(arr, start, medium)

    # Find largest sub array in right
    mr = find_max_sub(arr, medium + 1, end)

    # Find largest sub array which start in left and end in right of array
    mm = find_max_left(arr, start, medium) + find_max_right(arr, medium + 1, end)

    return max_these(ml, mr, mm)


# find largest sub array with ending is left of array
def find_max_left(arr, start, end):
    sum_t = 0
    max_left = arr[end]
    for i in range(end, start - 1, -1):
        sum_t += arr[i]
        if sum_t > max_left:
            max_left = sum_t
    return max_left


def find_max_right(arr, start, end):
    sum_t = 0
    max_right = arr[start]
    for i in range(start, end + 1):
        sum_t += arr[i]
        if sum_t > max_right:
            max_right = sum_t
    return max_right


def max_these(a1, a2, a3):
    max_t = a1
    if max_t < a2:
        max_t = a2
    if max_t < a3:
        max_t = a3
    return max_t


# Test
arr_test = [-2, 11, -4, 13, -5, 2]
max_sub = find_largest_sub_arr(arr_test)
print('max: ', max_sub)

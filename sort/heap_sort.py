# Implement heap sort in python3
# Author Ton Quang Tu


def sort(arr):
    n = len(arr)
    heap_sort(arr, n)

    print(arr)


# Sorting increase
def heap_sort(arr, n):
    build_max_heap(arr, n)

    for i in range(n - 1, -1, -1):
        swap(arr, 0, i)
        max_heapify(arr, 0, i)


# Build heap for node i
# Recursive compare node i with 2*i + 1 and 2*i + 2
def max_heapify(arr, i, n):
    swap_index = i
    if 2 * i + 1 < n and arr[swap_index] < arr[2 * i + 1]:
        swap_index = 2 * i + 1

    if 2 * i + 2 < n and arr[swap_index] < arr[2 * i + 2]:
        swap_index = 2 * i + 2

    if swap_index != i:
        swap(arr, i, swap_index)
        max_heapify(arr, swap_index, n)


# To build max heap, we loop from n/2 -> 0. build max heap for each node
def build_max_heap(arr, n):
    for i in range(int(n/2), -1, -1):
        max_heapify(arr, i, n)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# Testing heap sort
test_arr = [23, 45, 35, 15, 13, 12, 15, 7, 9]
print("Array before sorting")
print(test_arr)
print("--------------------------------------")
print("Array after sorting")
sort(test_arr)


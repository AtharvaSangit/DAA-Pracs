### USE SEPERATE CELLS TO EXWCUTE BOTH METHODS ###
## RANDOMIZED ##
import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition_left(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, high)
    return i

def partition_right(arr, low, high):
    random.seed()
    r = low + random.randint(0, high - low)
    swap(arr, r, high)
    return partition_left(arr, low, high)

def quicksort(arr, low, high):
    if low < high:
        p = partition_right(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()


arr = [6, 4, 12, 8, 15, 16]
n = len(arr)
print("OUTPUT")
print("Original array: ")
print_array(arr)
quicksort(arr, 0, n - 1)
print("Sorted array: ")
print_array(arr)


## DETERMINISTIC ##

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)


arr = [12, 4, 5, 6, 7, 3, 1, 15, 8, 9, 2, 10]
n = len(arr)
print("OUTPUT")
print("Original array: ", end="")
for num in arr:
    print(num, end=" ")
print()

quicksort(arr, 0, n - 1)

print("Sorted array: ", end="")
for num in arr:
    print(num, end=" ")
print()

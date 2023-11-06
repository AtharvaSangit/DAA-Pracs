### USE SEPERATE CELLS TO EXWCUTE BOTH METHODS ###
## DETERMINISTIC ##
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partitionDet(arr, l, r):
  pivot = arr[r]
  i = l-1
  j=l
  while j<r:
    if arr[j]<pivot:
      i=i+1
      swap(arr, i, j)
    j+=1
  swap(arr, i+1, r)
  return i+1


def quicksortDet(arr, l, r):
  if l<r:
    pivot = partitionDet(arr,l,r)
    quicksortDet(arr, l, pivot-1)
    quicksortDet(arr, pivot, r)

arr = [6, 4, 12, 8, 15]

print(arr)
quicksortDet(arr,0,len(arr)-1)
print(arr)


## RANDOMIZED ##

import random

def partitionRandom(arr, l, r):
  pivot_index = random.randint(l, r)
  pivot = arr[pivot_index]
  i = l-1
  j=l
  while j<r:
    if arr[j]<pivot:
      i=i+1
      swap(arr, i, j)
    j+=1
  swap(arr, i+1, r)
  return i+1


def quicksortRandom(arr, l, r):
  if l<r:
    pivot = partitionRandom(arr,l,r)
    quicksortRandom(arr, l, pivot-1)
    quicksortRandom(arr, pivot, r)

arr = [65, 14, 5, 88, 125, 116]

print(arr)
quicksortRandom(arr,0,len(arr)-1)
print(arr)

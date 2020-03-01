import random
import time

# # SORTING ALGORITHMS

# # Bubble

# def bubbleSort(arr):
#     n = len(arr)

#     # Traverse through all array elements
#     for i in range(n):

#         # Last i elements are already in place
#         for j in range(0, n - i - 1):

#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
a = list(range(1000000))

# print(bubbleSort())
b = random.shuffle(a)
# print(sorted(a))

for i in range(len(a)):
    print(a[i])
    time.sleep(1)
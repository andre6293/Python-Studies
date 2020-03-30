# Andre Pinto
# Brazil, MAR/27/2020
# Exercise from the book:
# Grokking Algorithms - An Illustrated Guide For Programmers and Other Curious People
# A book by Aditya Y. Bhargava

# The array needs to be sorted in order to use binary search.


def binary_search(item, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((high + low) / 2)
        if item > arr[mid]:
            low = mid + 1
        elif item == arr[mid]:
            return mid
        else:
            high = mid - 1

# Andre Pinto
# Brazil, MAR/29/2020
# Exercise from the book:
# Grokking Algorithms - An Illustrated Guide For Programmers and Other Curious People
# A book by Aditya Y. Bhargava
#
# 4.3 Find the maximum number in a list.

def maximum_n(arr):
    return arr[0] if len(arr) == 1 else \
        arr[0] if arr[0] > maximum_n(arr[1:]) else maximum_n(arr[1:])

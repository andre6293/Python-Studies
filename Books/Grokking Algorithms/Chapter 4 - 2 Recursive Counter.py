# Andre Pinto
# Brazil, MAR/29/2020
# Exercise from the book:
# Grokking Algorithms - An Illustrated Guide For Programmers and Other Curious People
# A book by Aditya Y. Bhargava
#
# 4.2 Write a recursive function to count the number of items in a list.

def recursive_counter(arr):
    return 1 if len(arr) == 1 else 1 + recursive_counter(arr[1:])

# Andre Pinto
# Brazil, MAR/29/2020
# Exercise from the book:
# Grokking Algorithms - An Illustrated Guide For Programmers and Other Curious People
# A book by Aditya Y. Bhargava

def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])

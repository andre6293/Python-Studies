# Andre Pinto
# Brazil, MAR/28/2020
# Exercise from the book:
# Grokking Algorithms - An Illustrated Guide For Programmers and Other Curious People
# A book by Aditya Y. Bhargava

## CORRIGIR

def selection_sort(arr):
    start = 0
    while start < len(arr):
        menor = arr[start]
        for i in range(start, len(arr)):
            if arr[i] < menor:
                menor = arr[i]
                menor_i = i
        arr[start], arr[menor_i] = arr[menor_i], arr[start]
        start += 1
    return arr

a = [3, 5, 2, 6, 9]

print(selection_sort(a))

# Andre Pinto
# Brazil, MAR/30/2020
# Exercise from the book:
# Grokking Algorithms - An Illustrated Guide For Programmers and Other Curious People
# A book by Aditya Y. Bhargava
#
# 4.4 Binary search using recursive.

def binary_recursion(item, arr):
    # low = 0
    # high = len(arr) - 1
    # while low <= high:
    #     mid = int((high + low) / 2)
    #     if item > arr[mid]:
    #         low = mid + 1
    #     elif item == arr[mid]:
    #         return mid
    #     else:
    #         high = mid - 1


x = "pupunha"
y = ["abacate", "abacaxi", "açaí", "acerola", "amora", "araticum", "bacaba",
     "banana", "biribá", "cacau", "cajá", "caqui", "carambola", "cereja",
     "cidra", "coco", "cupuaçu", "figo", "framboesa", "goiaba", "groselha",
     "ingá", "jabuticaba", "jaca", "jambo", "jenipapo", "kiwi", "laranja",
     "limão", "maçã", "mamão", "manga", "mangaba", "maracujá", "melancia",
     "melão", "morango", "pequi", "pera", "pêssego", "pitanga", "pitaya",
     "pupunha", "romã", "siriguela", "tâmara", "tamarindo", "tangerina",
     "tucumã", "uva verde"]

print(binary_recursion(x, y))

# Andre Pinto
# 08/10/2019
# a function to find numbers that are less than ten in an array

def lessthanten(a):
    list = []
    for i in range(len(a)):
        if a[i] < 5:
            list.append(a[i])

    return list

# Andre Pinto
# 04/10/2019
# Problem_002
# https://projecteuler.net/problem=2

def even_fibonacci(terms):

    list_all = []
    list_even = []

    for i in range(1, terms):
        if i == 1 or i==2:
            list_all.append(i)

        else:
            a = list_all[-1]+list_all[-2]
            list_all.append(a)

    for i in range(len(list_all)):
        if list_all[i] % 2 == 0:
            list_even.append(list_all[i])

    return sum(list_even)

print(even_fibonacci(33))

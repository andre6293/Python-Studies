# Andre Pinto
# 01/05/2020
# https://www.hackerrank.com/challenges/mini-max-sum

def miniMaxSum(arr):
    order = sorted(arr)
    minimum = sum(list(order)[0:4])
    maximum = sum(list(order)[1:5])
    return str(minimum) + " " + str(maximum)


# Teste
x = [7, 69, 2, 221, 8974]
print(sorted(x))
print(miniMaxSum(x))
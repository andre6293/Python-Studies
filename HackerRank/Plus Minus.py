# Andre Pinto
# 01/05/2020
# https://www.hackerrank.com/challenges/plus-minus

def plusMinus(arr):
    more_count = len([i for i in arr if i > 0])
    less_count = len([i for i in arr if i < 0])
    equal_count = len([i for i in arr if i == 0])
    return (
        str(more_count / len(arr)) + "\n" +
        str(less_count / len(arr)) + "\n" +
        str(equal_count / len(arr))
    )

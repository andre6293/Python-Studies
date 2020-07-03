# Andre Pinto
# 03/12/2019
# https://www.hackerrank.com/challenges/compare-the-triplets

def compareTriplets(a, b):
    r_array = [0, 0]

    for i in range(3):
        if a[i] > b[i]:
            r_array[0] += 1
        elif a[i] == b[i]:
            pass
        else:
            r_array[1] += 1
    return r_array


a, b = [17, 28, 30], [99, 16, 8]

print(compareTriplets(a, b))

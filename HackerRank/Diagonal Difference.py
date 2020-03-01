def diagonalDifference(arr):
    return abs(a[0][0] + a[2][2] - a[0][2] - a[2][0])


a = [[1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]]

print(diagonalDifference(a))

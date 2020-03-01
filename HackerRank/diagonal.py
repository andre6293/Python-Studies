def diagonalDifference(arr):
    matrixlen = len(arr)
    diagonal1 = 0
    diagonal2 = 0

    # diagonal 1 value
    for i in range(matrixlen):
        diagonal1 += arr[i][i]

    # diagonal 2 value
    for i in range(matrixlen):
        diagonal2 += arr[i][len(arr) - i - 1]
    return abs(diagonal1 - diagonal2)

print(diagonalDifference(ar))

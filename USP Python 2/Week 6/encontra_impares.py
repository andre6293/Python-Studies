def encontra_impares(arr):
    impares = []
    if len(arr) < 2:
        return arr
    else:
        return impares.extend(encontra_impares(arr[1:]))
    return impares


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(encontra_impares(a))

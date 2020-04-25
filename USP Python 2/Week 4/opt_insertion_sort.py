def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        k = i
        while k > 0 and chave < arr[k - 1]:
            arr[k] = arr [k - 1]
            k -= 1
        arr[k] = chave
    return arr

x = [3, 2, 4, 6, 1]
print(insertion_sort(x))

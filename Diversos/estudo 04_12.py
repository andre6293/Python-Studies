def multiply_array(a, b):
    if len(a) != len(b):
        return "Invalid command. Arrays must have the same length."

    f = []
    for i in range(len(a)):
        f.append(a[i] * b[i])
    return f


a = [2, 4, 6, 8, 9, 6]
b = [22, 14, 64, 86, 59, 25]


print(multiply_array(a, b))

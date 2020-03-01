def maximo(a, b, c):
    maximo = 0
    if a > b:
        maximo = a
    else:
        maximo = b
    if maximo > c:
        return maximo
    else:
        return c

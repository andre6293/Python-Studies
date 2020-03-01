# Kangaroo
# x = posição inicial
# v = velocidade


def kangaroo(x1, v1, x2, v2):
    x = 0
    if x1 > x2 and v1 > v2:
        return "NO"
    elif x2 > x1 and v2 > v1:
        return "NO"
    else:
        while x < 10000:
            x1 += v1
            x2 += v2
            if x1 == x2:
                return "YES"
            else:
                x += 1
        return "NO"


print(kangaroo(0, 2, 5, 3))

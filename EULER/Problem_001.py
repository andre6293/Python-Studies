# Problem_001


def multiples_3and5(a, b):

    count = 0
    multiple_list = []

    for i in range(a, b):
        if i % 3 == 0 or i % 5 == 0:
            count += 1
            multiple_list.append(i)

    return str(count) + " multiples of 3 or 5 in this range. " \
                        "Their sum equals " + str(sum(multiple_list)) + "."


print(multiples_3and5(1, 1000))

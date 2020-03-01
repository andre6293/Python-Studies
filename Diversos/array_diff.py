# def array_diff(a,b):
#     for i in range(len(b)):
#         if b[i] in a:
#             for j in range(a.count(b[i])):
#                 a.remove(b[i])
#     return a

def array_diff(a,b):
    return [x for x in a if x not in b]

a = [1, 2]
b = [1]


print(array_diff(a,b))

def lessthanten(a):
    list = []
    
    for i in range(len(a)):
        if a[i] < 5:
            list.append(a[i])
            
    return list


print(lessthanten([1, 2, 3, 10]))
def fibo(to=10):
    a = 1
    b = 2
    for i in range(to):
        yield a
        a, b = b, a + b
        
print([i for i in fibo() if i % 2 == 0])
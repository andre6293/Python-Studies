num = input("Insira o número a ser testado: ")
if int(num) % 3 == 0 and int(num) % 5 == 0:
    print("FizzBuzz")
else:
    print(num)

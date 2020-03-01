# Variaveis
n = input("Digite um número inteiro: ")
rep = len(n)
final = 0

# Mecanismo
for i in range(rep):
    final += int(n[i])

print(final)

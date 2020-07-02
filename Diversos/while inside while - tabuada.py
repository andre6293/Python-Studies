# Andre Pinto
# 05/02/2020
# Tabuada
# gera um arquivo .txt com as tabuadas de 1 a 10

linha = 1
coluna = 1
addstr = ""

maximo = int(input("Até qual tabuada você gostaria de gerar?\n"))
while coluna <= maximo:
    while linha <= maximo:
        addstr += str(linha * coluna) + "\t"
        linha += 1
    addstr += "\n"
    coluna += 1
    linha = 1

f = open('tabuada.txt','w')
f.write(addstr)
# Tabuada

linha = 1
coluna = 1
addstr = ""

while coluna <= 10:
    while linha <= 10:
        addstr += str(linha * coluna) + "\t"
        linha += 1
    addstr += "\n"
    coluna += 1
    linha = 1

f = open('tabuada.txt','w')
f.write(addstr)
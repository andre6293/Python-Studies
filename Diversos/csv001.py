import csv
import re

with open(
    "Diversos\Lista Nominais\SED.txt",
        "r") as file:
    sed = file.read()

with open(
    "Diversos\Lista Nominais\eSEC.txt",
        "r") as file:
    esec = file.read()

sed_alunos = (re.sub(r"^\d* ", "", sed, 0, re.MULTILINE)).split("\n")
sed_numeracao = (re.sub(r" .*", "", sed, 0, re.MULTILINE)).split("\n")
esec_alunos = (re.sub(r"^\d* ", "", esec, 0, re.MULTILINE)).split("\n")
esec_numeracao = (re.sub(r" .*", "", esec, 0, re.MULTILINE)).split("\n")

rows = zip(sed_numeracao, sed_alunos, esec_numeracao, esec_alunos)

with open('deleteme.csv', "w", encoding="UTF-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(("N SED", "ALUNO SED", "N eSEC",
                     "ALUNO eSEC", "NUMERAÇÃO", "NOME"))
    writer.writerow(("", "", "", "",
                     '=SE(A2=C2;"OK";"ERRO")', '=SE(B2=D2;"OK";"ERRO")'))
    for row in rows:
        writer.writerow(row)
f.close()
print("All done. :)")
# ANDRE PINTO
# 20/03/2020

import re
from openpyxl import Workbook


def corrige_esec(str):
    regex = r'(Prefeitura.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*)|(EMEF.*\n.*\n)'
    result = re.sub(regex, '', str)
    regex = r'\n'
    result = re.sub(regex, '', result, 1)
    regex = r' \d\d.*'
    result = re.sub(regex, '', result)
    regex = r'(?<=\n)\d\d/.*\n'
    result = re.sub(regex, '', result)
    regex = r'\n(?=\D)(?!\W)'
    result = re.sub(regex, ' ', result)
    result = "eSEC\n" + result
    return result


def corrige_sed(str):
    regex = r"(Ano Leti.*\n.*\n.*\n.*)|(Ativos.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n)"
    result = re.sub(regex, '', str)
    regex = r'\n'
    result = re.sub(regex, '', result, 1)
    regex = r'(Turma:.)|((?<= ANO )\d)|(.......ANUAL)'
    result = re.sub(regex, '', result)
    regex = r'\n(?=000)'
    result = re.sub(regex, ' ', result)
    regex = r'\n(?=[^0-9])(?!\n)'
    result = re.sub(regex, ' ', result)
    regex = r'(?<=Õ) |(?<=Ç) |(?<=Ã) (?=\w)(?!\w\w\w)'
    result = re.sub(regex, '', result)
    regex = r' 000.*'
    result = re.sub(regex, '', result)
    regex = r'\d (?=\d)'
    result = re.sub(regex, '', result)
    regex = r'°'
    result = re.sub(regex, 'º', result)
    result = "SED\n" + result
    return result


# FORMATANDO AS LISTAS PARA A CONFECÇÃO DA PLANILHA
with open('lista_esec.txt', 'r') as file:
    esec = file.read()
    esec = corrige_esec(esec)

with open('lista_sed.txt', 'r') as file:
    sed = file.read()
    sed = corrige_sed(sed)

# CRIANDO A PLANILHA
wb = Workbook()
filepath = "Comparador.xlsx"
sheet = wb.active

# INSERINDO OS VALORES
sed = sed.split(sep="\n")
esec = esec.split(sep="\n")
sheet_rows = []

for i in range(len(sed)):
    entry = sed[i], esec[i]
    sheet_rows.append(entry)

for line in sheet_rows:
    sheet.append(line)

# FÓRMULAS DE COMPARAÇÃO
for i in range(999):
    entry = '=IF(A' + str(i+2) + '=B' + str(i+2) + ',"","ERRO")'
    cell = "C" + str(i + 2)
    sheet[cell] = entry

# FORMATAÇÃO
sheet.column_dimensions['A'].width = 65
sheet.column_dimensions['B'].width = 65
sheet.column_dimensions['C'].width = 25

# EXPORTAÇÃO
wb.save(filepath)
print("Concluído!")

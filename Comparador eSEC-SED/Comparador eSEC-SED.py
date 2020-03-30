# ANDRE PINTO
# 20/03/2020

import re
from openpyxl import Workbook
from openpyxl.styles import Font


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
    regex = r'(Ano Leti.*\n.*\n.*\n.*)|(Ativos.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n)'
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
for i in range(998):
    entry = '=IF(B' + str(i + 4) + '=C' + str(i + 4) + ',"","ERRO")'
    cell = "C" + str(i + 3)
    sheet[cell] = entry

# FORMATAÇÃO
sheet['C1'] = "OBS."
sheet.insert_cols(1)
sheet.insert_rows(1)
sheet.column_dimensions['A'].width = 4
sheet.column_dimensions['B'].width = 65
sheet.column_dimensions['C'].width = 65
sheet.column_dimensions['D'].width = 25
sheet.row_dimensions[2].height = 30
sheet.row_dimensions[2].font = Font(name="Calibri", bold=True, size=20)

# EXPORTAÇÃO
wb.save(filepath)
print("Concluído!")

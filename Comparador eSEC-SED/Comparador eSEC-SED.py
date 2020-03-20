import re
from openpyxl import Workbook


# Formatando as listas para a confecção da planilha
def corrige_esec(str):
    regex = r'(Prefeitura.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*)|(EMEF.*\n.*\n)'
    result = re.sub(regex, '', str)
    regex = r'\n'
    result = re.sub(regex, '', result, 1)
    regex = r' \d\d/.*'
    result = re.sub(regex, '', result)
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
    regex = r' 000.*'
    result = re.sub(regex, '', result)
    regex = r'\d (?=\d)'
    result = re.sub(regex, '', result)
    regex = r'°'
    result = re.sub(regex, 'º', result)
    return result


with open('D:\Programacao\Python\Comparador eSEC-SED\lista_esec.txt', 'r') as file:
    esec = file.read()
    esec = corrige_esec(esec)

with open('D:\Programacao\Python\Comparador eSEC-SED\lista_sed.txt', 'r') as file:
    sed = file.read()
    sed = corrige_sed(sed)

# Criando a planilha
wb = Workbook()
filepath = "demo.xlsx"
wb.save(filepath)

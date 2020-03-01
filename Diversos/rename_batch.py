import os

months = {
    1 : 'Janeiro',
    2 : 'Fevereiro',
    3 : 'Março',
    4 : 'Abril',
    5 : 'Maio',
    6 : 'Junho',
    7 : 'Julho',
    8 : 'Agosto',
    9 : 'Setembro',
    10 : 'Outubro',
    11 : 'Novembro',
    12 : 'Dezembro'
    }

def rename_date(directory):

    files = os.listdir(directory)
    for x in range(len(files)):
        title_num = int(files[x][11:13])
        
        return months[title_num]



folder = r'C:\Users\Ander\Desktop\Nova pasta'

#print(rename_date(folder)[0][11:13])

print(rename_date(folder))
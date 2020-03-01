import os

def rename_date(direct):
    files = os.listdir(direct)
    return files

folder = "C:\Users\Ander\Desktop\Nova pasta"

print(rename_date(folder))
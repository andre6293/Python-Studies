# Andre Pinto
# 26/02/2020
# Name Generator
import json
import random


names = json.loads(open("names.json").read()) # names list must be in the same folder
surnames = json.loads(open("surnames.json").read()) # surnames list also must be in the same folder

namecount = 0
generated = []
while namecount < 1000:
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    name = "".join((str(names[x]) + " " + str(surnames[y])))
    generated.append(name)
    namecount += 1

f = open('generated_names.json', 'w') # it creates a file with the generated names
f.write(str(generated))

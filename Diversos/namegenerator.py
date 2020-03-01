# Name Generator
import json
import random


names = json.loads(open("names.json").read())
surnames = json.loads(open("surnames.json").read())

namecount = 0
generated = []
while namecount < 1000:
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    name = "".join((str(names[x]) + " " + str(surnames[y])))
    generated.append(name)
    namecount += 1

f = open('generated_names.json', 'w')
f.write(str(generated))

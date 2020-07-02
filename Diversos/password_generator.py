# Andre Pinto
# 13/01/2020
# Password generator
# It can be called with or without the length argument through terminal/cmd/bash

import sys
import random
import string

sys.tracebacklimit = 0
source = list(string.ascii_letters + string.digits + string.punctuation)
length = 0

if len(sys.argv) > 1:
    length = sys.argv[1]
    if not length.isdigit() or int(length) <= 0 or int(length) > 100:
        print("Invalid input. Please enter a number between 1 and 100\n")
else:
    while True:
        length = input("How many characters would you like in your password?\n")
        if not length.isdigit() or int(length) <= 0 or int(length) > 100:
            print("Please input a number between 1 and 100")
        else:
            break
n = 1
while n != '0':
    random.SystemRandom().shuffle(source)
    password = "".join(source[0:int(length)])
    print("\nSua senha é:\n" + password + "\n")
    n = input(
        "Digite qualquer coisa para uma nova senha. Digite 0 para sair. \n")

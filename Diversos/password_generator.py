import random
import string

source = list(string.ascii_letters + string.digits + string.punctuation)

n = 1
while n != 0:
    random.SystemRandom().shuffle(source)
    password = "".join(source[0:8])
    print(password + "\n")
    n = input(
        "Digite qualquer coisa para uma nova senha. Digite 0 para sair. \n")

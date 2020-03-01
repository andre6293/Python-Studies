import time
import json
import random
import string
import os

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = (os.urandom(1024))

names = json.loads(open("names.json").read())
providers = json.loads(open("providers.json").read())

for name in names:
    name_extra = " ".join(random.choice(string.digits))
    email = random.choice(providers)

    username = name.lower() + name_extra + email
    password = "".join(random.choice(chars) for i in
                       range(random.choice(range(5, 10))))

    print(username)
    print(password)
    time.sleep(1)

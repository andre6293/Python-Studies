import re
import json
import time

email_list = json.loads(open("email_list.json").read())

logins = []

for i in range(len(email_list)):
    reg_result = re.sub("@.*", "", email_list[i])
    logins.append(reg_result)

print(logins[:4])

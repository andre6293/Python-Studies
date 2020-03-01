def timeConversion(s):
    hr = s[:2]
    resto = s[2:8]
    am = "AM" in s
    if not am and int(hr) < 12:
        return str(int(hr) + 12) + resto
    elif int(hr) == 12 and am:
        return "00" + resto
    else:
        return hr + resto


Hora = input("Qual a hora que deseja converter?" + "\n")
print(timeConversion(Hora))

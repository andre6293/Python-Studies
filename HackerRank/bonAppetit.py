# Andre Pinto
# 26/05/2020
# https://www.hackerrank.com/challenges/birthday-cake-candles

def bonAppetit (pratos, iAnnaNaoComeu, precos, cobrado):
    amountOfPeople = 2
    totalADividir = (sum(precos) - precos[iAnnaNaoComeu]) / amountOfPeople
    if totalADividir < cobrado:
        return cobrado - totalADividir
    return "Bon Appetit"

a = 4
b = 1
c = [3, 10, 2, 9]
d = 6

print(bonAppetit(a, b, c, d))


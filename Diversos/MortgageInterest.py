# Andre Pinto
# 

import math

def mortgage_calc ():
    percent = 100
    monthsInYear = 12

    principal = int(input("Principal ($1K - $1M): "))
    monthlyInterestRate = float(input("Annual interest Rate: ")) / percent / monthsInYear
    period = int(input("Period (Years): "))
    result = principal * monthlyInterestRate * math.pow((1 + monthlyInterestRate), period) / (math.pow((1 + monthlyInterestRate), period) - 1)
    print("Mortgate: " + "${:,.2f}".format(result))
    return result

mortgage_calc()


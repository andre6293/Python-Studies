# Andre Pinto
# 07/12/2019
# https://www.hackerrank.com/challenges/birthday-cake-candles

def birthdayCakeCandles(ar):
    maxc = 0
    for i in range(len(ar)):
        if ar[i] > maxc:
            maxc = ar[i]
    return ar.count(maxc)


candles = [3, 2, 1, 3]
print(birthdayCakeCandles(candles))
print(len(candles))

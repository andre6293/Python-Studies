# Andre Pinto
# 02/12/2019
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013


def find_next_square(sq):
    whole = int(sq ** 0.5)
    if whole == sq ** 0.5:
        return (whole + 1) * (whole + 1)
    return -1

# Andre Pinto
# 08/12/2019
# https://www.hackerrank.com/challenges/staircase

def staircase(n):
    result = []
    for i in range(1, n+1):
        spaces = n - i
        sharps = n - spaces
        line = (" " * spaces + "#" * sharps)
        result.append(line)
    return "\n".join(result)

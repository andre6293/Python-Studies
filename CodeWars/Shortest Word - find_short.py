# Andre Pinto
# 02/12/2019

def find_short(s):
    return min(len(x) for x in s.split())

a = "Artyom rose reluctantly from his seat by the fire and (...) headed  towards  the  darkness."

print(find_short(a))
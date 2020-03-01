# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data 
# types.


# def find_short(s):
#     sortedwords = sorted(s.split(), key=len)
#     return len(sortedwords[0])

def find_short(s):
    return min(len(x) for x in s.split())

a = "bitcoin take over the world maybe who knows perhaps"

print(find_short(a))
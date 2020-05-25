# Breaking the Records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Andre Pinto
# 22/05/2020

def breakingRecords (scores):
    lowest = scores[0]
    highest = scores[0]
    low_count = 0
    high_count = 0

    for i in range(1, len(scores)):
        if scores[i] > highest:
            highest = scores[i]
            high_count += 1
        elif scores[i] < lowest:
            lowest = scores[i]
            low_count += 1
    return high_count, low_count
def divisible_sum_pairs(n, k, ar):
    pairs = 0
    for i in range(n):
        for j in range(1, n):
            if ar[i] < ar[j] and (ar[i] + ar[j]) % k == 0:
                pairs += 1
    return pairs


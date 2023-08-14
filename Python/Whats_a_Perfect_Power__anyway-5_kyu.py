# https://www.codewars.com/kata/54d4c8b08776e4ad92000835
# 2023-08-01T18:05:28.247+0000
def isPP(n):
    for m in range(2, int(n**0.5) + 1):
        k = 2
        while m**k <= n:
            if m**k == n:
                return [m, k]
            k += 1
    return None
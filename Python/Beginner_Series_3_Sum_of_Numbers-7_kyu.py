# https://www.codewars.com/kata/55f2b110f61eb01779000053
def get_sum(a,b):
    a, b = min(a, b), max(a, b)
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum
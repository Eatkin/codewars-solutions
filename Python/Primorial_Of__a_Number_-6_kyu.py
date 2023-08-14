# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124
# 2023-08-04T19:32:05.999+0000
from math import prod
# Thanks Stack Exchange
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True

def num_primorial(n):
    # Find first n primes
    primes = [2]
    n -= 1
    num = 3
    while n > 0:
        if is_prime(num):
            primes.append(num)
            n -= 1
        num += 2
    return prod(primes)
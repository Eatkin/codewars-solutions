# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
import functools

def persistence(n):
    reductions = 0
    while n > 9:
        n = functools.reduce(lambda a, b: int(a)*int(b),str(n))
        reductions += 1
    
    return reductions
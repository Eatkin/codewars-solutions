# https://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b
# 2023-08-02T06:37:59.628+0000
from math import log2, floor
def score(n):
    if n == 0:
        return 0
    
    largest = 2**floor(log2(n))
    carry = largest >> 1
    while carry >= 1:
        largest |= carry
        carry = carry >> 1
    
    return largest
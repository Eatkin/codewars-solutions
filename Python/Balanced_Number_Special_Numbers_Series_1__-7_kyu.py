# https://www.codewars.com/kata/5a4e3782880385ba68000018
# 2023-08-04T18:39:46.231+0000
from math import ceil, floor
def balanced_num(number):
    number = str(number)
    if len(number) <= 2:
        return 'Balanced'
    start = number[:floor((len(number) - 1) / 2)]
    end = number[ceil((len(number)) / 2) + (1 - len(number) % 2):]
    
    return 'Balanced' if sum([int(n) for n in start]) == sum([int(n) for n in end]) else 'Not Balanced'
    
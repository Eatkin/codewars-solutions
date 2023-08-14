# https://www.codewars.com/kata/562926c855ca9fdc4800005b
# 2023-07-30T17:59:30.699+0000
def number_to_pwr(number, p): 
    return number * number_to_pwr(number, p - 1) if p > 0 else 1
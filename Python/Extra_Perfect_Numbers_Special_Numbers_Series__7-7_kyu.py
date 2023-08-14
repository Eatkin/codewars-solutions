# https://www.codewars.com/kata/5a662a02e626c54e87000123
# 2023-08-04T19:17:18.897+0000
def extra_perfect(n):
    return [x for x in range(n + 1) if x & 1 == 1]
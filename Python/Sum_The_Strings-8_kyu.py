# https://www.codewars.com/kata/5966e33c4e686b508700002d
def sum_str(a, b):
    return str(sum([int(x) if x else 0 for x in [a, b]]))
# https://www.codewars.com/kata/577bd026df78c19bca0002c0
def correct(s):
    return s.translate(str.maketrans("501", "SOI"))
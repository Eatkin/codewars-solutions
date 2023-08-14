# https://www.codewars.com/kata/5a4d303f880385399b000001
# 2023-08-04T19:03:16.427+0000
def fact(n):
    n = int(n)
    return n * fact(n - 1) if n > 1 else 1
def strong_num(number):
    return "STRONG!!!!" if sum(map(fact, str(number))) == number else "Not Strong !!"
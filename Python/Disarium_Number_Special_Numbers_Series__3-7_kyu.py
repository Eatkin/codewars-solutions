# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003
# 2023-08-04T19:10:54.326+0000
def disarium_number(number):
    return 'Disarium !!' if sum([int(n) ** (i + 1) for i, n in enumerate(str(number))]) == number else 'Not !!'
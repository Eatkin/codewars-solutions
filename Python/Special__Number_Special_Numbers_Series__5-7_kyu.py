# https://www.codewars.com/kata/5a55f04be6be383a50000187
# 2023-08-04T19:14:43.650+0000
def special_number(number):
    return "Special!!" if all([int(n) < 6 for n in str(number)]) else "NOT!!"
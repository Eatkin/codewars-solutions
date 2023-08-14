# https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed
# 2023-08-04T19:13:25.665+0000
def jumping_number(number):
    number = str(number)
    jumping = True
    n = number[0]
    for m in number[1:]:
        if abs(int(n) - int(m)) != 1:
            return "Not!!"
        n = m
    return "Jumping!!"
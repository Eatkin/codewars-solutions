# https://www.codewars.com/kata/570e8ec4127ad143660001fd
# 2023-07-30T18:01:01.960+0000
def billboard(name, price=30):
    return price + billboard(name[1:], price=price) if len(name) > 1 else price
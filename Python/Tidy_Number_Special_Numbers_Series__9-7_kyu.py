# https://www.codewars.com/kata/5a87449ab1710171300000fd
# 2023-08-04T19:18:52.466+0000
def tidyNumber(n):
    n = str(n)
    prev = n[0]
    for x in n[1:]:
        if x < prev:
            return False
        prev = x
    return True
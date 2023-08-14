# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0
# 2023-08-06T13:39:40.696+0000
def last(s):
    return sorted(s.split(), key=lambda x: x[-1])
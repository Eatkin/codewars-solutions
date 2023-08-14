# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118
# 2023-08-03T16:25:20.182+0000
from collections import OrderedDict
def distinct(seq):
    return list(OrderedDict.fromkeys(seq))
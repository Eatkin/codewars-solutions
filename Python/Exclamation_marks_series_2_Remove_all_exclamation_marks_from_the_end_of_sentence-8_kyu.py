# https://www.codewars.com/kata/57faece99610ced690000165
# 2023-08-02T11:51:13.336+0000
import re
def remove(s):
    return re.sub(r'!*$', '', s)
# https://www.codewars.com/kata/596c6eb85b0f515834000049
# 2023-06-16T14:09:42.007+0000
import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)
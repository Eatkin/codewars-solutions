# https://www.codewars.com/kata/567bf4f7ee34510f69000032
import re
def is_digit(n):
    return re.search(r"^[0-9]$", n) is not None and len(n) == 1
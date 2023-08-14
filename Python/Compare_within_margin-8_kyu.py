# https://www.codewars.com/kata/56453a12fcee9a6c4700009c
# 2023-08-05T17:54:53.213+0000
def close_compare(a, b, margin = 0):
    return 0 if abs(a-b) <= margin else -1 if a < b else 1
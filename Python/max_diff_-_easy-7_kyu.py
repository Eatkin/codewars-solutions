# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095
# 2023-08-05T17:59:04.837+0000
def max_diff(lst):
    if not lst:
        return 0
    return max(lst) - min(lst)
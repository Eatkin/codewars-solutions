# https://www.codewars.com/kata/580a4734d6df748060000045
# 2023-08-03T16:26:41.421+0000
def is_sorted_and_how(arr):
    return "yes, ascending" if arr == sorted(arr) else "yes, descending" if arr == sorted(arr, reverse = True) else "no"
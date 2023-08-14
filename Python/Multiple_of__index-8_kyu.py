# https://www.codewars.com/kata/5a34b80155519e1a00000009
# 2023-06-19T05:48:31.825+0000
def multiple_of_index(arr):
    return [elem for i, elem in enumerate(arr) if elem == i or (i > 0 and abs(elem) % i == 0)]
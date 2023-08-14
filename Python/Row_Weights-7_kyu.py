# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
# 2023-08-05T18:02:38.782+0000
def row_weights(array):
    return (sum([n for i, n in enumerate(array) if i % 2 == 0]), sum([n for i, n in enumerate(array) if i % 2 == 1]))
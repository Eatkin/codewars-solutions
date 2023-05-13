# https://www.codewars.com/kata/578553c3a1b8d5c40300037c
def binary_array_to_number(arr):
    integer = 0
    for i, bin in enumerate(arr):
        integer += bin<<(len(arr) - i - 1)
    return integer
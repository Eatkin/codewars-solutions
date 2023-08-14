# https://www.codewars.com/kata/5a4138acf28b82aa43000117
# 2023-06-15T13:39:11.618+0000
def adjacent_element_product(array):
    maxseen = array[0] * array[1]
    for i in range(1, len(array) - 1):
        maxseen = max(array[i] * array[i + 1], maxseen)
        
    return maxseen
        
# https://www.codewars.com/kata/57f609022f4d534f05000024
def stray(arr):
    result = 0
    for elem in arr:
        result ^= elem
        
    return result
# https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):
    #your code here
    return [elem for elem in a if not elem in b]
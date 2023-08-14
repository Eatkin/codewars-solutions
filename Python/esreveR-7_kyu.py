# https://www.codewars.com/kata/5413759479ba273f8100003d
# 2023-08-05T18:06:05.628+0000
def reverse(lst):
    # Swap elements
    for i in range(len(lst) // 2):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]
        
    return lst
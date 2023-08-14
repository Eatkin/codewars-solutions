# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
# 2023-06-15T17:47:32.444+0000
def clean_string(s):
    poop = ''
    # Naive solution but its all good
    for char in s:
        if char == '#':
            poop = poop[:-1]
        else:
            poop += char
    return poop
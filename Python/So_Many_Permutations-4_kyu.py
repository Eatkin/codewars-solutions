# https://www.codewars.com/kata/5254ca2719453dcc0b00027d
def permutations(s):
    if len(s) == 1:
        return [s]
    output_set = set()
    for i, letter in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            output_set.add(letter + perm)
    return list(output_set)
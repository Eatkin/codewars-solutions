# https://www.codewars.com/kata/52efefcbcdf57161d4000091
def count(s):
    char_dict = {}
    for c in s:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
            
    return char_dict
        
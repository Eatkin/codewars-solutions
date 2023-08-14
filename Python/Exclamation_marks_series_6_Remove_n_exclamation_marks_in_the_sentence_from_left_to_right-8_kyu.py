# https://www.codewars.com/kata/57faf7275c991027af000679
# 2023-08-04T11:25:14.122+0000
def remove(s, n):
    new_string = ""
    for c in s:
        if n > 0 and c == "!":
            n -= 1
            continue
        new_string += c
    
    return new_string
        
            
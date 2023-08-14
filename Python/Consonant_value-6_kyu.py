# https://www.codewars.com/kata/59c633e7dcc4053512000073
# 2023-08-02T13:27:54.400+0000
def solve(s):
    count = 0
    highest = 0
    offset = 96
    vowels = "aeiou"
    for c in s:
        if c in vowels:
            if count > highest:
                highest = count
            count = 0
            continue
        count += ord(c) - offset
        
    # Final check
    if count > highest:
        highest = count
        
    return highest
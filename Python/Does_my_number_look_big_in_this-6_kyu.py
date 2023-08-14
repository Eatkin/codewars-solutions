# https://www.codewars.com/kata/5287e858c6b5a9678200083c
# 2023-06-15T17:12:16.945+0000
def narcissistic( value ):
    # Trivial
    if abs(value) < 10:
        return True
    
    cache = {}
    
    digits = str(value)
    exponent = len(digits)
    sum = 0
    for num in digits:
        if num in cache:
            sum += cache[num]
        else:
            cache[num] = int(num) ** exponent
            sum += cache[num]
        
        if sum > value:
            return False
        
    if sum == value:
        return True
    return False
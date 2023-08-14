# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
# 2023-08-03T09:14:06.064+0000
def up_array(arr):
    # Validation
    if not arr:
        return None
    if any([True if x < 0 or x > 9 else False for x in arr]):
        return None
    
    index = 1
    try:
        while arr[-index] == 9:
            arr[-index] = 0
            index += 1
        # Add the carry
        arr[-index] += 1
    except:
        # This happens when we exceed array bounds
        arr = [1] + arr
    
    return arr
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
def is_square(n):    
    # Trivial cases
    if n < 0:
        return False
    if n == 0:
        return True
    
    # Try a binary search algorithm
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 == n:
            return True
        if mid ** 2 < n:
            left = mid + 1
        else:
            right = mid - 1
        
    return False
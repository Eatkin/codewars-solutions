# https://www.codewars.com/kata/56a921fa8c5167d8e7000053
def password(string):    
    if len(string) < 8:
        return False
    # Gather lists of things
    chars = [char for char in string if not char.isnumeric()]
    nums = [char for char in string if char.isnumeric()]
    uppers = [char for char in chars if char == char.upper()]
    lowers = [char for char in chars if char == char.lower()]
    if not uppers or not lowers or not nums:
        return False
    
    return True
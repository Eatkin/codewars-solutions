# https://www.codewars.com/kata/566044325f8fddc1c000002c
def even_chars(st): 
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    
    return [char for i, char in enumerate(st) if i%2 == 1]
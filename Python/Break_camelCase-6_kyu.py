# https://www.codewars.com/kata/5208f99aee097e6552000148
def solution(s):
    formatted_string = ""
    for char in s:
        if char == char.upper():
            formatted_string += " "
        formatted_string += char
    
    return formatted_string
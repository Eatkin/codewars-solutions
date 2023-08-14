# https://www.codewars.com/kata/5839edaa6754d6fec10000a2
# 2023-06-15T08:17:40.152+0000
def find_missing_letter(chars):
    # Get the first letter char code
    first_letter_code = ord(chars[0])
    is_upper = chars[0].isupper()
    # Get a list of letters
    letters = [chr(num).upper() if is_upper else chr(num) for num in range(first_letter_code, 123)]
    # Now compare
    for letter in letters:
        if letter not in chars:
            return letter
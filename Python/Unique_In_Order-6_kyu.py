# https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(sequence):
    return [sequence[char] for char in range(len(sequence)) if char == 0 or sequence[char] != sequence[char - 1]]
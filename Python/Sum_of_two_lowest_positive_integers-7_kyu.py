# https://www.codewars.com/kata/558fc85d8fd1938afb000014
def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))
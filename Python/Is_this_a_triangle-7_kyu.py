# https://www.codewars.com/kata/56606694ec01347ce800001b
def is_triangle(a, b, c):
    # Use triangle inequality
    return sorted([a, b, c])[-1] < sum(sorted([a, b, c])[:2])
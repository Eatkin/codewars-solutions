# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
def expression_matter(a, b, c):
    # Find the largest combination of a, b and c
    combos = [a + b + c,
              a * b * c,
              a + (b * c),
              (a + b) * c,
              a * (b + c),
              (a * b) + c]
    return max(combos)
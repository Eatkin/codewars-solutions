# https://www.codewars.com/kata/54d7660d2daf68c619000d95
# 2023-08-02T13:38:38.683+0000
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return (a * b) // calculate_gcd(a, b)

def convert_fracts(lst):
    if not lst:
        return []

    # Calculate the least common multiple (LCM) of denominators
    cd = lst[0][1]
    for fraction in lst[1:]:
        cd = calculate_lcm(cd, fraction[1])

    # Prepare the output list
    result = []
    for numerator, denominator in lst:
        factor = cd // denominator
        result.append([numerator * factor, cd])

    return result

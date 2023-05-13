# https://www.codewars.com/kata/563f037412e5ada593000114
def calculate_years(principal, interest, tax, desired):
    years = 0
    total = principal
    while total < desired:
        total *= (1 + interest * (1 - tax))
        years += 1
        
    return years
# https://www.codewars.com/kata/555eded1ad94b00403000071
def real_series_sum(n):
    if n <= 0:
        return 0
    
    summation = (3*n - 2) ** -1
    if summation != 1:
        summation += real_series_sum(n - 1)
    
    return summation

# The string formatting requirement makes recursion really annoying so yeah
def series_sum(n):
    return "%0.2f" % real_series_sum(n)
# https://www.codewars.com/kata/54da5a58ea159efa38000836
from collections import Counter
def find_it(seq):
    dict = Counter(seq)
    for num, occurences in dict.items():
        if occurences%2 != 0:
            return num
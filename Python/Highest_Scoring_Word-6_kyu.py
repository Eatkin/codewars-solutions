# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
def high(x):
    return sorted(x.split(), key = lambda w: sum([ord(c) - 96 for c in w]), reverse = True)[0]
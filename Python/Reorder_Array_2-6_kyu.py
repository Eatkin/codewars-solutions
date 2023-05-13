# https://www.codewars.com/kata/5a48fab7bdb9b5b3690009b6
import numpy as np

def reorder(a, b):
    return [list(np.roll(np.linspace(0, a//2 - 1, a//2, dtype = int), b)), list(np.roll(np.linspace(a//2, a - 1, a//2, dtype = int),b))]
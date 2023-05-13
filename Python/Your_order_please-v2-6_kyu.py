# https://www.codewars.com/kata/55c45be3b2079eccff00010f
import re
def order(sentence):
    return "" if not sentence else " ".join(sorted(sentence.split(), key = lambda word: re.findall(r"\d", word)))
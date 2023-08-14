# https://www.codewars.com/kata/56b3b27cadd4ad275500000c
# 2023-06-15T17:45:50.640+0000
import re
def word_count(s):
    banned_words = ['a', 'the', 'on', 'at', 'of', 'upon', 'in', 'as']
    # Replace any non-words with spaces
    pattern = re.compile(r'[^a-zA-Z]')
    s = re.sub(pattern, ' ', s)
    s = [s for s in s.split() if s.lower() not in banned_words]
    return len(s)
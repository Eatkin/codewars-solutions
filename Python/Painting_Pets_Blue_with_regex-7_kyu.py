# https://www.codewars.com/kata/6361bdb5d41160000ee6db86
# Each of the given inputs will be a word of 
# mixed case characters followed by either `cat` or `dog`.

search = r"\b(\w+)\b(?=\s+cat)|\b(\w+)\b(?=\s+dog)" 

substitute = "blue"
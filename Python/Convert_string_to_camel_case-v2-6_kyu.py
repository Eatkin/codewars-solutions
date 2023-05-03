# /kata/517abf86da9663f1d2000003
import re

def to_camel_case(text):
    regex = r'[\W]+|_+'
    return "".join([word.capitalize() if i > 0 else word for i, word in enumerate(re.split(regex, text))])
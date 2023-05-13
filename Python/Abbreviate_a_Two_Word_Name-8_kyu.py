# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
import re
def abbrev_name(name):
    return ".".join(re.findall(r"\b(\w)", name)).upper()
    
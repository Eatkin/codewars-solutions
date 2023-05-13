# https://www.codewars.com/kata/52fba66badcd10859f00097e
import re
def disemvowel(string_):
    return re.sub(r"[aeiou]", "", string_, flags = re.IGNORECASE)
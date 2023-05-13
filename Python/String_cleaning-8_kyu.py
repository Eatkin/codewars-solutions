# https://www.codewars.com/kata/57e1e61ba396b3727c000251
import re
def string_clean(s):
    """
    Function will return the cleaned string
    """
    regex = re.compile(r"\d+")
    s = re.sub(regex, "", s)
    return s
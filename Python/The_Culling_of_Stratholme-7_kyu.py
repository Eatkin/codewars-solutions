# https://www.codewars.com/kata/634913db7611b9003dff49ad
import re
def purify(s: str) -> str:
    return re.sub(r" {2,}", " ", re.sub(r"\w[iI]+\w|[iI]+\w|\w[iI]+|[iI]+", "", s).strip())
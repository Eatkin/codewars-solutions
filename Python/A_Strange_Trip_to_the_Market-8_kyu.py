# https://www.codewars.com/kata/55ccdf1512938ce3ac000056
import re
def is_lock_ness_monster(string):
    print(string)
    pattern = re.compile(r"(tree fiddy)|(3\.50)|(three fifty)")
    return re.search(pattern, string) is not None
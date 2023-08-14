# https://www.codewars.com/kata/56dbe0e313c2f63be4000b25
# 2023-08-02T11:47:15.383+0000
def vert_mirror(strng):
    return "\n".join([s[::-1] for s in strng.split("\n")])
def hor_mirror(strng):
    return "\n".join(strng.split("\n")[::-1])
def oper(fct, s):
    return fct(s)
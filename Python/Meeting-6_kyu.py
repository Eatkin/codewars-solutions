# https://www.codewars.com/kata/59df2f8f08c6cec835000012
# 2023-07-30T18:04:04.390+0000
def meeting(s):
    names = s.split(";")
    return "".join(sorted([f"({name.split(':')[1].upper()}, {name.split(':')[0].upper()})" for name in names]))
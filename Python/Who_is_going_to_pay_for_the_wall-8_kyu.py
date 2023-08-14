# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7
# 2023-08-05T18:00:57.031+0000
def who_is_paying(name):
    lst = [name, name[:2]]
    return lst if len(name) > 2 else [lst[0]]
# https://www.codewars.com/kata/57a6633153ba33189e000074
# 2023-08-02T14:35:54.950+0000
def ordered_count(inp):
    counts = []
    cache = set()
    for char in inp:
        if char not in cache:
            cache.add(char)
            counts.append((char, inp.count(char)))
    return counts
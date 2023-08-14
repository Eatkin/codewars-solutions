# https://www.codewars.com/kata/5a58d889880385c2f40000aa
# 2023-08-04T18:31:17.933+0000
def automorphic(n):
    return "Automorphic" if str(n) == str(n ** 2)[-len(str(n)):] else "Not!!"
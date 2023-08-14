# https://www.codewars.com/kata/58223370aef9fc03fd000071
# 2023-08-06T13:47:04.344+0000
def dashatize(n):
    if not isinstance(n, int):
        return "None"
    n = list(str(n).strip("-"))
    n = "".join([x if int(x) % 2 == 0 else f'-{x}-' for x in n])
    return n.strip("-").replace("--", "-")
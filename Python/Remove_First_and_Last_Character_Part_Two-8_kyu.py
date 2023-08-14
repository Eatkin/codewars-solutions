# https://www.codewars.com/kata/570597e258b58f6edc00230d
# 2023-08-03T16:23:20.752+0000
def array(string):
    return " ".join(string.split(",")[1:-1]) if string.count(",") > 1 else None
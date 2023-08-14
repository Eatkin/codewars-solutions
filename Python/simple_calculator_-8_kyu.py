# https://www.codewars.com/kata/5810085c533d69f4980001cf
# 2023-06-16T16:31:26.291+0000
def calculator(x,y,op):
    if not isinstance(x, int) or not isinstance(y, int):
        return 'unknown value'
    match op:
        case '+':
            return x+y
        case '-':
            return x-y
        case '*':
            return x*y
        case '/':
            return x/y
        case _:
            return "unknown value"
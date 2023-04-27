# https://www.codewars.com/kata/57e3f79c9cb119374600046b
def hello(name=""):
    return f"Hello, {name[0].upper() + name[1:].lower()}!" if name else "Hello, World!"
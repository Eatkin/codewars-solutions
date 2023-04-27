# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
def number(lines):
    if len(lines) == 0:
        return []
    
    return [f"{i + 1}: {line}" for i, line in enumerate(lines)]
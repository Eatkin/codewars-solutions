# https://www.codewars.com/kata/59377c53e66267c8f6000027
# 2023-06-16T09:12:28.323+0000
def alphabet_war(fight):
    values = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1,
        'm': -4,
        'q': -3,
        'd': -2,
        'z': -1
    }
    
    score = 0
    for char in fight:
        score += values.get(char, 0)
        
    return "Let's fight again!" if score == 0 else "Left side wins!" if score > 0 else "Right side wins!"
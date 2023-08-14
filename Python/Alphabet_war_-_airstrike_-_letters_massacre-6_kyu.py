# https://www.codewars.com/kata/5938f5b606c3033f4700015a
# 2023-06-16T09:14:41.557+0000
import re
def alphabet_war(fight):
    pattern = r'(\w?\*\w?)'
    fight = re.sub(pattern, '', fight)

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
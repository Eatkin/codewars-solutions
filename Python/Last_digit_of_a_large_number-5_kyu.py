# https://www.codewars.com/kata/5511b2f550906349a70004e1
# 2023-06-15T08:08:16.630+0000
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    # Truncate
    n1 = int(str(n1)[-1])
    # Keep track of cyclic patterns
    patterns = [n1]
    pattern_break = False
    truncated = n1
    for i in range(n2 - 1):
        truncated *= n1
        # Truncate
        truncated = int(str(truncated)[-1])
        # Add n1 to the pattern
        patterns.append(truncated)
        # We are looking for a twice repeat of a pattern so we can determine the periodicity
        print(patterns)
        if patterns[:len(patterns) // 2] == patterns[len(patterns) // 2:]:
            pattern_break = True
            break
            
    if pattern_break:
        period = len(patterns) // 2
        return patterns[(n2 - 1) % period]
    
    return truncated
# https://www.codewars.com/kata/5324945e2ece5e1f32000370
# 2023-06-15T14:19:33.533+0000
def sum_strings(x, y):
    x = x.lstrip('0')
    y = y.lstrip('0')
    
    if x == '':
        x = '0'
    if y == '':
        y = '0'
        
    digits = "0123456789"
    digit_map = {c: i for i, c in enumerate(digits)}
        
    x_width, y_width = len(x), len(y)
    max_width = max(x_width, y_width)
    # Pad
    x = x.rjust(max_width, '0')
    y = y.rjust(max_width, '0')
    
    total_sum = []
    carry = 0
    for i in range(max_width - 1, -1, -1):
        x_digit = digit_map[x[i]]
        y_digit = digit_map[y[i]]
        
        digit_sum = x_digit + y_digit + carry
        total_sum.append(str(digit_sum % 10))
        carry = digit_sum // 10
    
    if carry > 0:
        total_sum.append(str(carry))
    
    return ''.join(total_sum[::-1])
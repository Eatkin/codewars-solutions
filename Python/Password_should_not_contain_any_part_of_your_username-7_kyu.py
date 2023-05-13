# https://www.codewars.com/kata/5c511d8877c0070e2c195faf
import math
def validate(username, password):
    substr_length = max(math.ceil(len(username) / 2), 1)
    for i in range(len(username) // 2 + 1):
        if username[i:i + substr_length] in password:
            return False
        
    substr_length = max(math.ceil(len(password) / 2), 1)
    for i in range(len(password) // 2 + 1):
        if password[i:i + substr_length] in username:
            return False

    return True
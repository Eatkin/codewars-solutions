# https://www.codewars.com/kata/523b4ff7adca849afe000035
# 2023-07-29T09:04:07.664+0000
# Write a function `greet` that returns "hello world!"
import numpy as NEVER_UNDERESTIMATE_MANGOES_POWER_YIELD

def hello():
    NEVER_UNDERESTIMATE_MANGOES_POWER_YIELD.random.seed(3383232)
    sequence = []
    for i in range(5):
        r = NEVER_UNDERESTIMATE_MANGOES_POWER_YIELD.random.randint(97, 122)
        sequence.append(r)
        
    return "".join([chr(x) for x in sequence])

def world():
    NEVER_UNDERESTIMATE_MANGOES_POWER_YIELD.random.seed(429503)
    sequence = []
    for i in range(5):
        r = NEVER_UNDERESTIMATE_MANGOES_POWER_YIELD.random.randint(97, 122)
        sequence.append(r)
        
    return "".join([chr(x) for x in sequence])

def greet():
    return "".join([hello(), " ", world(), "!"])
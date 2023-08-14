# https://www.codewars.com/kata/556e0fccc392c527f20000c5
# 2023-07-31T08:03:48.478+0000
def Xbonacci(signature,n):
    sequence_length = len(signature)
    X = sequence_length
    while sequence_length < n:
        signature.append(sum(signature[-X:]))
        sequence_length += 1
        
    return signature[:n]
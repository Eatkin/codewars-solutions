# https://www.codewars.com/kata/54da539698b8a2ad76000228
def is_valid_walk(walk):
    #determine if walk is valid
    return len(walk) == 10 and walk.count("n") - walk.count("s") == 0 and walk.count("e") - walk.count("w") == 0
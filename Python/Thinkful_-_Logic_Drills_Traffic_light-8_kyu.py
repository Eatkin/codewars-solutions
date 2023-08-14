# https://www.codewars.com/kata/58649884a1659ed6cb000072
# 2023-06-20T16:20:15.962+0000
def update_light(current):
    return ["green", "yellow", "red"][(["green", "yellow", "red"].index(current) + 1) % 3]
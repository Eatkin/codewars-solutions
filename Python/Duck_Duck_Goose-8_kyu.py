# https://www.codewars.com/kata/582e0e592029ea10530009ce
# 2023-08-02T16:29:10.678+0000
def duck_duck_goose(players, goose):
    return players[goose % len(players) - 1].name
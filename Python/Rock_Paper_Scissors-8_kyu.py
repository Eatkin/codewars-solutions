# https://www.codewars.com/kata/5672a98bdbdd995fad00000f
def rps(p1, p2):
    rps_list = ["rock", "paper", "scissors"]
    diff = abs(rps_list.index(p1) - rps_list.index(p2))
    if diff == 0:
        return "Draw!"
    if diff == 1:
        return "Player 1 won!" if rps_list.index(p1) > rps_list.index(p2) else "Player 2 won!"
    return "Player 1 won!" if rps_list.index(p1) < rps_list.index(p2) else "Player 2 won!"
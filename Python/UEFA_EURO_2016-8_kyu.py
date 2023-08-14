# https://www.codewars.com/kata/57613fb1033d766171000d60
# 2023-08-05T17:57:02.749+0000
def uefa_euro_2016(teams, scores):
    win_status = f"{teams[0]} won!" if scores[0] > scores[1] else f"{teams[1]} won!" if scores[1] > scores[0] else "teams played draw."
    return f"At match {teams[0]} - {teams[1]}, {win_status}"
    
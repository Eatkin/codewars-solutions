# https://www.codewars.com/kata/5853213063adbd1b9b0000be
# 2023-08-07T09:07:13.359+0000
def street_fighter_selection(fighters, initial_position, moves):
    width = len(fighters[0])
    height = len(fighters)
    # I'm changing this to (x, y) coordinates because it makes more sense to me that way
    pos = (initial_position[1], initial_position[0])
    moves_dict = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)
    }
    selection = []
    # Horrible
    for move in moves:
        pos = ((pos[0] + moves_dict[move][0]) % width, min(height - 1, max(0, pos[1] + moves_dict[move][1])))
        selection.append(fighters[pos[1]][pos[0]])
        
    return selection
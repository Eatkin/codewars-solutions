# https://www.codewars.com/kata/576757b1df89ecf5bd00073b
def tower_builder(n_floors):
    tower_list = []
    for i in range(n_floors):
        tower_list.append(" " * i + "*" *  (2 * (n_floors - i) - 1) + " " * i)
        
    tower_list.reverse()
    return tower_list
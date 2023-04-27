# https://www.codewars.com/kata/5acbc3b3481ebb23a400007d
def is_flush(cards):
    # Get the final character of each card
    suits = [card[-1] for card in cards]
    # Return if all suits are the same
    return len(set(suits)) == 1
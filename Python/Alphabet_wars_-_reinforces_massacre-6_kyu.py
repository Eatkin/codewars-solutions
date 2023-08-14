# https://www.codewars.com/kata/593e2077edf0d3e2d500002d
# 2023-06-19T09:04:06.868+0000
def alphabet_war(reinforces, airstrikes):
    battlefield = list(reinforces.pop(0))   # Remove the first element from the list
    field_size = len(battlefield)
    
    # Kind of a shit solution because of all the loops but hey it works
    for i, strike in enumerate(airstrikes):
        # Action the strike first
        for j, char in enumerate(strike):
            # Kill the troops
            if char == '*':
                battlefield[max(0, j - 1)] = '_'
                battlefield[j] = '_'
                battlefield[min(field_size - 1, j + 1)] = '_'
        
        # Replace the troops with the reinforcements
        for j, troops in enumerate(reinforces):
            new_reinforces = list(troops)
            for k, letter in enumerate(troops):
                if battlefield[k] == '_' and letter != '_':
                    battlefield[k] = letter
                    new_reinforces[k] = '_'
            # If we've done all we can get rid of them
            reinforces[j] = "".join(new_reinforces)
            if battlefield.count('_') == 0:
                break
                
    return "".join(battlefield)
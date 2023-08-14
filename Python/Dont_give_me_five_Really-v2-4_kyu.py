# https://www.codewars.com/kata/621f89cc94d4e3001bb99ef4
# 2023-06-14T17:08:52.993+0000
def dont_give_me_five(start, end):
    # Precalculated number of digits that aren't 5 over various intervals
    # Dictionary key represents the number of trailing 0's
    CUMULATIVE_COUNTS = {1: 9, 2: 81, 3: 729, 4: 6561, 5: 59049, 6: 531441, 7: 4782969, 8: 43046721, 9: 387420489, 10: 3486784401, 11: 31381059609, 12: 282429536481, 13: 2541865828329, 14: 22876792454961, 15: 205891132094649, 16: 1853020188851841, 17: 16677181699666569, 18: 150094635296999121, 19: 1350851717672992089, 20: 12157665459056928801}
    
    # Observations:
    # 9 numbers without 5 between 0-10
    # -> 90 between 0-100 but we need to remove 9 for 50-59 -> 81
    # -> 810 between 0-1000 but we need to remove 81 for 500-599, therefor be 729
    # So we can iteratively calculate these
    """
    # Just a method for pre-calculating the digits
    def cumulative_sum_counts(digits):
        for i in range(digits):
            try:
                CUMULATIVE_COUNTS[i + 1]
            except:
                CUMULATIVE_COUNTS[i + 1] = CUMULATIVE_COUNTS[i] * 9
    
    cumulative_sum_counts(19)
    print(CUMULATIVE_COUNTS)
    """
    
    # Edge cases - numbers are < 10, just use a naive solution
    # "Crossing the line" - we cross 0 in the range, add one extra digit
    # Start and end are negative - make them positive and flip them    
    if start < 0 and end < 0:
        start, end = abs(end), abs(start)
    
    # This is required to be inclusive of start
    ss = start
    if start > 0:
        start -= 1
    
    def count_not_fives(num):
        num = abs(num)
        if num < 5:
            return num
        elif num == 5:
            return 4
        elif num < 10:
            return num - 1

        # Otherwise we will need to iterate over each digit
        # E.g. 257 - we count the 200s, then we add 5 * 10 - 1 because the next digit is 5
        # E.g. 638 - We count 1000, then minus 4 * 100 off that (because 6 > 5), count 3 * 10, then count num not 5s in 8
        num = str(num)
        significance = len(num) - 1
        sequence_length = 0
        # We don't care about the last number
        for i in range(len(num) - 1):
            digit = int(num[i])
            if digit < 5:
                sequence_length += digit * CUMULATIVE_COUNTS[significance]
            elif digit == 5:
                sequence_length += digit * CUMULATIVE_COUNTS[significance] - 1
                # Every trailing digit no longer needs to be counted
                return sequence_length
            else:
                sequence_length += CUMULATIVE_COUNTS[significance + 1]
                sequence_length -= (10 - digit) * CUMULATIVE_COUNTS[significance]

            significance -= 1

        # Add on the last little bit
        sequence_length += count_not_fives(int(num[-1]))
        return sequence_length
    
    # So now we have a good method
    start_sequence = count_not_fives(start)
    end_sequence = count_not_fives(end)
    
    if ss <= 0:
        return end_sequence + start_sequence + 1
    return end_sequence - start_sequence
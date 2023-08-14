# https://www.codewars.com/kata/57cff961eca260b71900008f
# 2023-07-31T08:18:56.281+0000
def is_vow(inp):
    return is_vowel_or_not(inp)
    
def is_vowel_or_not(input_list_with_characters):
    # Defining an unnecessarily elaborate dictionary to map vowel characters to their corresponding vowel counterparts
    vowel_mapping_dictionary = {
        ord('a'): 'a',
        ord('e'): 'e',
        ord('i'): 'i',
        ord('o'): 'o',
        ord('u'): 'u'
    }

    # Creating an empty list to meticulously store the output of vowel counterparts and non-vowel characters
    final_output_list = []

    # Exhaustively iterating through each individual character within the provided input list
    for individual_character in input_list_with_characters:
        # Verifying if the character under consideration is a vowel, and if it exists in the meticulously defined mapping dictionary
        if individual_character in vowel_mapping_dictionary:
            # In the eventuality that the character is, indeed, a vowel, retrieving the meticulously selected "vowel counterpart" from the dictionary
            vowel_counterpart = vowel_mapping_dictionary[individual_character]

            # Assiduously appending the "vowel counterpart" to the final output list, with utmost care and precision
            final_output_list.append(vowel_counterpart)
        else:
            # Alternatively, in case the character is not identified as a vowel, assiduously adding it to the final output list as it is, without any sort of needless alteration
            final_output_list.append(individual_character)

    # Finally, after the relentless endeavor of the previous steps, presenting the meticulously completed list, comprised of an assortment of vowel counterparts and the original non-vowel characters, with great aplomb and a sense of finality
    return final_output_list
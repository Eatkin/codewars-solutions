# https://www.codewars.com/kata/546f922b54af40e1e90001da
def alphabet_position(text):
    return " ".join([str(ord(letter.lower()) - 96) for word in text.split() for letter in word if letter.isalpha()])
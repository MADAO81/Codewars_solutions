# https://www.codewars.com/kata/59859f435f5d18ede7000050/train/python


# def word_to_bin(word):
#     return [ f"{ord(c):08b}" for c in word ]



def word_to_bin(word):
    return [format(ord(ch), '08b') for ch in word]

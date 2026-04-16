# https://www.codewars.com/kata/5d41e16d8bad42002208fe1a/train/python


# def more_zeros(s):
#     chars = [c for c in s if bin(ord(c)).count("0") >= 5]
#     uniques = []
#     for ch in chars:
#         if ch not in uniques:
#             uniques.append(ch)
#     return uniques



# def more_zeros(s):
#     return [v for i,v in enumerate(s) if bin(ord(v))[2:].count('0') > bin(ord(v))[2:].count('1') and v not in s[:i]]



def more_zeros(s):
    results = []
    
    for letter in s:
        dec_repr = bin(ord(letter))[2:]
        if (dec_repr.count("0") > dec_repr.count("1")) and (letter not in results):
            results.append(letter)
    
    return results

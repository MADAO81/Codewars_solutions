# https://www.codewars.com/kata/597bb84522bc93b71e00007e/train/python

# def string_merge(string1, string2, letter):
#     string1 = [string1[0:i] for i, n in enumerate(string1) if n == letter]        
#     string2 = [string2[i:] for i, n in enumerate(string2) if n == letter]
#     return string1[0] + string2[0]


# def StringMerge(str1, str2, ltr):
#     return str1.split(ltr)[0] + ltr + str2.split(ltr, 1)[1]

def StringMerge(string1, string2, letter):
    return string1[:string1.index(letter)] + string2[string2.index(letter):]

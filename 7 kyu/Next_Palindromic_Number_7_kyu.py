# https://www.codewars.com/kata/56a6ce697c05fb4667000029/train/python


# Solution 1

# def palindrome(n):
#     s = str(n)
#     return s[::-1] == s

# def next_pal(val):
#     val += 1
#     while not palindrome(val):
#         val += 1
#     return val


# Solution 2

# from itertools import count

# def next_pal(val):
#     return next(c for c in count(val + 1) if str(c) == str(c)[::-1])


# Solution 3

def next_pal(val):
    val +=1
    while str(val) !=str(val)[::-1]:
        val +=1
    return val


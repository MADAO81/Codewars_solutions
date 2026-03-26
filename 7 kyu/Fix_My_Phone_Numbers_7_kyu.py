# https://www.codewars.com/kata/596343a24489a8b2a00000a2/train/python


# def is_it_a_num(s: str) -> str:
#     digits = ''.join(c for c in s if c.isdigit())
#     if len(digits)!=11 or not digits or digits[0] != '0':
#         return "Not a phone number"
#     else:
#         return digits



# from functools import partial
# from re import compile

# REGEX = partial(compile(r"\D+").sub, "")

# def is_it_a_num(s: str) -> str:
#     res = REGEX(s)
#     if len(res) == 11 and res[0] == "0":
#         return res
#     return "Not a phone number"



  def is_it_a_num(s: str) -> str:
    t = ''.join(i for i in s if i.isdigit())
    return t if len(t)==11 and t[0]=="0" else "Not a phone number"

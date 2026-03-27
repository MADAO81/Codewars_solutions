# https://www.codewars.com/kata/58ddffda929dfc2cae0000a5

# def clonewars(kata_per_day):
#     clone_qty = 1
#     kata = 0
#     while kata_per_day:
#         kata += kata_per_day * clone_qty
#         kata_per_day -= 1
#         if kata_per_day:
#             clone_qty += clone_qty
#     return [clone_qty, kata]

def clonewars(kata_per_day):
    return [2**max(kata_per_day-1,0),2**(kata_per_day+1)-kata_per_day-2]

# https://www.codewars.com/kata/57f625992f4d53c24200070e/train/python

# def bingo(ticket,win):
#     count = 0
#     for i in ticket:
#         for j in i[0]:
#             if ord(j)==i[1]:
#                 count +=1
#                 break
#     return "Winner!" if count >= win else "Loser!"


def bingo(ticket, win):
    return 'Winner!' if sum(chr(n) in s for s, n in ticket) >= win else 'Loser!'

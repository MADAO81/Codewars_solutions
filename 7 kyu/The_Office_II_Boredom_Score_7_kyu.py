# https://www.codewars.com/kata/57ed4cef7b45ef8774000014/train/python


def boredom(staff):
    d = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    score = sum(d[s] for s in staff.values())
    if score <= 80:
        return "kill me now"
    elif 80 < score < 100:
        return "i can handle this"
    else:
        return "party time!!"

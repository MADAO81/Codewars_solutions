# https://www.codewars.com/kata/57873ab5e55533a2890000c7/train/python

# import re


# def time_correct(t):
#     if not t:
#         return t
    
#     if not re.match("\d\d:\d\d:\d\d$", t):
#         return None
        
#     hours, minutes, seconds = [int(x) for x in t.split(':')]
    
#     if seconds >= 60:
#         minutes += 1
#         seconds -= 60
#     if minutes >= 60:
#         hours += 1
#         minutes -= 60
#     if hours >= 24:
#         hours = hours % 24
    
#     return "{0:0>2}:{1:0>2}:{2:0>2}".format(hours, minutes, seconds)



def time_correct(t):
    if not t: 
        return t
    try:
        h, m, s = map(int, t.split(':'))
        if s >= 60: s -= 60; m += 1
        if m >= 60: m -= 60; h += 1
        return '%02d:%02d:%02d' % (h % 24, m, s)
    except: 
        pass

# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

# import math
# def race(v1, v2, g):
#     if v1 >= v2:
#         return None
#     else:
#         time = g * 3600 / (v2 - v1)
#         h = time / 3600
#         mn = (time % 3600) / 60
#         s = time % 60
#         time_required = [math.floor(h), math.floor(mn), math.floor(s)]
#     return time_required


# def race(v1, v2, g):
#     t = 3600 * g/(v2-v1)
#     return [t/3600, t/60%60, t%60] if v2 > v1 else None



from datetime import datetime, timedelta

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g*3600/(v2-v1))))
        d = datetime(1,1,1) + sec
        
        return [d.hour, d.minute, d.second]

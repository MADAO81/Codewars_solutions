# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python




# def goodVsEvil(good, evil):

#     points_good = [1, 2, 3, 3, 4, 10]
#     points_evil = [1, 2, 2, 2, 3, 5, 10]
    
#     good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
#     evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])

#     result = 'Battle Result: '
    
#     if good < evil:
#         return result +'Evil eradicates all trace of Good'
#     elif good > evil:
#         return result + 'Good triumphs over Evil'
#     else:
#         return result + 'No victor on this battle field'


def good_vs_evil(good, evil):
    good = map(int,good.split(" "))
    evil = map(int,evil.split(" "))
    good_total = sum(map( lambda x: x[0]*x[1], zip(good, [1,2,3,3,4,10])))
    evil_total = sum(map( lambda x: x[0]*x[1], zip(evil, [1,2,2,2,3,5,10])))
    if good_total > evil_total:
        return "Battle Result: Good triumphs over Evil"
    elif good_total < evil_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

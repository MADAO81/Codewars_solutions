# https://www.codewars.com/kata/586e1d458cb711f0a800033b/train/python

# def process_data(data):
#     flat_lst =[item for sublist in data for item in sublist]
#     multipliers = [flat_lst[i]-flat_lst[i+1] for i in range(0,len(flat_lst),2)]
#     result = 1
#     for i in multipliers:
#         result *=i
#     return result



# from functools import reduce
# from itertools import starmap
# from operator import mul, sub

# def process_data(data):
#     return reduce(mul, starmap(sub, data))



def process_data(data):
    r = 1
    for d in data:
        r *= d[0] - d[1]
    return r

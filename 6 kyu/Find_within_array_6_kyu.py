# https://www.codewars.com/kata/51f082ba7297b8f07f000001/train/python

# def find_in_array(seq, predicate): 
#     rv = [i for i,x in enumerate(seq) if predicate(x,i)]
#     if rv == []: 
#         return -1
#     return rv[0]



# def find_in_array(seq, predicate): 
#     for index, value in enumerate(seq):
#         if predicate(value, index):
#             return index
#     return -1



def find_in_array(seq, fn): 
    return next((i for i, j in enumerate(seq) if fn(j, i)), -1)

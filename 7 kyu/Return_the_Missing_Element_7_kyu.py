# https://www.codewars.com/kata/5299413901337c637e000004/train/python


# def get_missing_element(seq): 
#     pattern = [0,1,2,3,4,5,6,7,8,9]
#     return list(set(pattern).difference(seq))[0]


# def get_missing_element(seq):
#     return set(range(10)).difference(seq).pop()
  

def get_missing_element(seq): 
    return 45 - sum(seq)

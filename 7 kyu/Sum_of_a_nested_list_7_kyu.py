# https://www.codewars.com/kata/5a15a4db06d5b6d33c000018/train/python

# def sum_nested(lst):
#     result = 0
#     for i in lst:
#         if isinstance(i,list):
#             result += sum_nested(i)
#         else:
#             result += i
#     return result

def sum_nested(lst):
	return sum(sum_nested(x) if isinstance(x,list) else x for x in lst)

# https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/python


# import math

# def buddy(start, limit):
# 	def sum_divisor(n):
# 		return int(sum((val+num for val,num in ((mas, n/mas) for mas in range(1, int(math.sqrt(n)) + 1) if n % mas == 0 and mas != n / mas))) - n)

# 	for y in range(start, limit+1):
# 		sum1 = sum_divisor(y)
# 		if sum_divisor(sum1 - 1) == y + 1 and sum1 - 1 > y:
# 			return [y, sum_divisor(y) - 1]
# 	return 'Nothing'




# def buddy(start, limit):
#     for n in range(start, limit + 1):
#         m = s(n)
#         if m > n and n == s(m):
#             return [n, m]
            
#     return "Nothing"
    
# def s(n):
#     s = 0
#     for i in range(2, round(n ** 0.5)):
#         if n % i == 0:
#             s += i
#             s += n // i
#     return s



def div_sum(n):
    divs = set()
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)

def buddy(start, limit):
    for n in range(start, limit+1):
        buddy = div_sum(n)
        
        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]
    
    return "Nothing"

# https://www.codewars.com/kata/573992c724fc289553000e95/train/python


# def action(s,x,y):
#     if x < y:
#         s = s[:x] + s[x+1:y+1] + s[x] + s[y+1:]
#     else:
#         s = s[:y] + s[x] + s[y:x] + s[x+1:]
#     return [int(s), x, y]


# def smallest(n):
#     n = str(n)
#     r = []
#     for i in range(len(n)):
#         for j in range(len(n)):
#             r.append(action(n,i,j))
#     return sorted(r)[0]



# def smallest(n):
#     s = list(str(n))
#     def swap(i, p):
#         t = s[:]
#         t.insert(i, t.pop(p))
#         return int(''.join(t))
#     return min([swap(i, p), p, i] for i in range(len(s)) for p in range(len(s)))



def smallest(n):
	s = str(n)
	min1, from1, to1 = n, 0, 0
	for i in range(len(s)):
		removed = s[:i] + s[i+1:]
		for j in range(len(removed)+1):
			num = int(removed[:j] + s[i] + removed[j:])
			if (num < min1):
				min1, from1, to1 = num, i, j
	return [min1, from1, to1]

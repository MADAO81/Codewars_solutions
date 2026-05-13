# https://www.codewars.com/kata/555624b601231dc7a400017a/train/python


# def josephus_survivor(n,k):
#     lst = [i for i in range(1,n+1)]
#     indx = 0
#     while len(lst) > 1:
#         indx = indx + k -1
#         indx = indx%len(lst)
#         lst.pop(indx)
#     return lst[0]
    
# def josephus(items,k):
#     indx = 0
#     permutation = []
#     while len(items) > 1:
#         indx = indx + k - 1
#         indx = indx%len(items)
#         permutation.append(items.pop(indx))
#     permutation.append(items[0])
#     return permutation


def josephus_survivor(n,k):
    v = 0
    for i in range(1, n + 1): 
        v = (v + k) % i
    return v + 1

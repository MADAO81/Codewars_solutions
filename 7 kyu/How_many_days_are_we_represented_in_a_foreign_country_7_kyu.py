# https://www.codewars.com/kata/58e93b4706db4d24ee000096/train/python

# def days_represented(trips: list[list[int]]) -> int:
#     represented_days = set()  
#     for arrival, departure in trips:
#         represented_days.update(range(arrival, departure + 1))
#     return len(represented_days)


def days_represented(trips):
    L=[]
    for i in trips:
        for j in range(i[0],i[1]+1):
            L.append(j)
    a=set(L)
    return len(a)

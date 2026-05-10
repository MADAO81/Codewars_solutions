# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035/train/python


# from math import sqrt, floor

# def tour(friends, friend_towns, home_to_town_distances):
#     distance = 0
#     n = [home_to_town_distances[t[1]] for f in friends for t in friend_towns if f == t[0]]
#     index = 0
#     for i in n:
#         if index < len(n) - 1:
#             distance += sqrt(round(abs(pow(i,2) - pow(n[index +1],2))))
#             index += 1
#     return floor(distance + n[0] + n[-1])
    

def tour(friends, friend_towns, home_to_town_distances):
    res=0
    s=0
    for i in friend_towns:
        if i[0] in friends:
            res=res+(home_to_town_distances[i[1]]**2-s**2)**(0.5)
            s=home_to_town_distances[i[1]]
    res=res+s
    return int(res)

# https://www.codewars.com/kata/58941fec8afa3618c9000184/train/python

# import math
# def growing_plant(up_speed, down_speed, desired_height):
#     total_height = 0
#     count = 1
#     days = 1
#     while total_height < desired_height:
#         if count == 1:
#             total_height += up_speed
#             count = 2
#         else:
#             total_height -= down_speed
#             count = 1
            
#         days += 1
        
#     return math.ceil(days/2)


def growing_plant(up_speed, down_speed, desired_height):
    days = 1
    height = up_speed
    while (height < desired_height):
        height += up_speed - down_speed
        days += 1
    return days

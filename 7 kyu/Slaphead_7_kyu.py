https://www.codewars.com/kata/57efab9acba9daa4d1000b30/train/python

# def bald(s):
#     hair_count = s.count('/')
#     s = s.replace('/','-')
#     if hair_count == 0:
#         message = "Clean!"
#     elif hair_count == 1:
#         message = "Unicorn!"
#     elif hair_count == 2:
#         message = "Homer!"
#     elif 3 <= hair_count <= 5:
#         message = "Careless!"
#     else:  # >5 hairs
#         message = "Hobo!"
#     return [s,message]


def bald(s):
    hair_names = {
        0: "Clean!",
        1: "Unicorn!",
        2: "Homer!",
        3: "Careless!",
        4: "Careless!",
        5: "Careless!",
    }
    return [s.replace("/","-"),"Hobo!"] if s.count("/") > 5 else [s.replace("/","-"), hair_names[s.count("/")]]

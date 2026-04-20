# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python

# def get_order(order):
#     menus = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
#     result = []
#     for i in range(len(menus)):
#         for j in range(len(order)):
#             substring = order[j:j + len(menus[i])]
            
#             if len(substring) != len(menus[i]):
#                 continue
                
#             if substring == menus[i]:
#                 result.append(substring.capitalize())
                
#     return " ".join(result)


def get_order(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    clean_order = ''
    for i in menu:
        clean_order += (i.capitalize() + ' ') * order.count(i)
    return clean_order[:-1]

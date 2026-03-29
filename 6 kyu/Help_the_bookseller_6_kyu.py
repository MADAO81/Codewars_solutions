# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python



# def stock_list(listOfArt, listOfCat):
#     if (len(listOfArt) == 0) or (len(listOfCat) == 0):
#         return ""
#     result = ""
#     for cat in listOfCat:
#         total = 0
#         for book in listOfArt:
#             if (book[0] == cat[0]):
#                 total += int(book.split(" ")[1])
#         if (len(result) != 0):
#             result += " - "
#         result += "(" + str(cat) + " : " + str(total) + ")"
#     return result


import re
def stock_list(stocklist, categories):
    total = dict()
    string = str()
    for letter in categories:
        regex = re.compile(r'^('+letter+').*\s(\d+)')
        for code in stocklist:
            mo = regex.findall(code)
            if mo:
                total[mo[0][0]] = total.get(mo[0][0], 0) + int(mo[0][1])
            else:
                total[letter] = total.get(letter, 0)
    for key, value in total.items():
        string += f'({key} : {value}) - '
    return string.rstrip(' - ') 

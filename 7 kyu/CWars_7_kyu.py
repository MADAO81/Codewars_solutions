#https://www.codewars.com/kata/55968ab32cf633c3f8000008/train/python


# def initials(name):
#     name = name.split()  
#     return '.'.join(el.title() if idx == len(name) - 1 else el[0].upper() for idx,el in enumerate(name))


def initials(name):
    names = name.split()
    return '.'.join(x[0].upper() for x in names) + names[-1][1:]

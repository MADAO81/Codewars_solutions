# https://www.codewars.com/kata/57fafb6d2b5314c839000195/train/python


# def remove(string):
#     result = []
#     for i in string.split(' '):
#         if i.count('!') != 1:
#             result.append(i)
#     return ' '.join(result)


# def remove(s):
#     return ' '.join(filter(lambda word: word.count('!') !=1, s.split(' ')))


def remove(s):
    return ' '.join(w for w in s.split(' ') if w.count('!') != 1)

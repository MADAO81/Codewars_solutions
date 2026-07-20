# https://www.codewars.com/kata/5dcde0b9fcb0d100349cb5c0/train/python

# '''
#     Write a function that returns the longest contiguous palindromic substring in s. 
#     In the event that there are multiple longest palindromic substrings, return the 
#     first to occur.
# '''

# # TODO: Complete in linear time xDD
# def longest_palindrome(s):
#     if not s:
#         return ""
    
#     # Преобразуем строку для обработки четных и нечетных палиндромов
#     # Вставляем разделители между символами и по краям
#     t = '#'.join('^{}$'.format(s))
#     n = len(t)
#     p = [0] * n  # массив радиусов палиндромов
#     center = right = 0  # центр и правая граница текущего палиндрома
    
#     for i in range(1, n - 1):
#         # Зеркальное отражение относительно центра
#         if right > i:
#             mirror = 2 * center - i
#             p[i] = min(right - i, p[mirror])
        
#         # Расширяем палиндром
#         while t[i + p[i] + 1] == t[i - p[i] - 1]:
#             p[i] += 1
        
#         # Обновляем центр и правую границу, если нашли больший палиндром
#         if i + p[i] > right:
#             center = i
#             right = i + p[i]
    
#     # Находим первый палиндром максимальной длины
#     max_len = 0
#     center_idx = 0
#     for i in range(1, n - 1):
#         if p[i] > max_len:
#             max_len = p[i]
#             center_idx = i
    
#     # Извлекаем палиндром из исходной строки
#     start = (center_idx - max_len) // 2
#     return s[start:start + max_len]



def longest_palindrome(s, sep=" "):
    # Interpolate some inert character between input characters
    # so we only have to find odd-length palindromes
    t = sep + sep.join(s) + sep

    r = 0       # Rightmost index in any palindrome found so far ...
    c = 0       # ... and the index of the centre of that palindrome.
    spans = []  # Length of the longest substring in T[i:] mirrored in T[i::-1]

    # Manacher's algorithm
    for i,_ in enumerate(t):
        span = min(spans[2*c-i], r-i-1) if i < r else 0
        while span <= i < len(t)-span and t[i-span] == t[i+span]:
            span += 1
        r, c = max((r, c), (i+span, i))
        spans.append(span)

    span = max(spans)
    middle = spans.index(span)

    return t[middle-span+1:middle+span].replace(sep, "") 

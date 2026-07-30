# https://www.codewars.com/kata/5886e082a836a691340000c3/train/python

# import math

# def rectangle_rotation(a, b):
#     # Находим максимальное целое k, такое что k^2 <= a^2/2
#     def floor_sqrt_half(n):
#         # n - четное число (a или b)
#         return math.isqrt(n * n // 2)
    
#     max_a = floor_sqrt_half(a)
#     max_b = floor_sqrt_half(b)
    
#     # Диапазон x: от -(a+b)//2 до (a+b)//2 достаточно
#     limit = (a + b) // 2 + 1
#     total = 0
    
#     for x in range(-limit, limit + 1):
#         # Из условия |x + y| <= max_a
#         y_min1 = -max_a - x
#         y_max1 = max_a - x
        
#         # Из условия |x - y| <= max_b
#         y_min2 = x - max_b
#         y_max2 = x + max_b
        
#         # Пересечение интервалов
#         y_min = max(y_min1, y_min2)
#         y_max = min(y_max1, y_max2)
        
#         if y_min <= y_max:
#             total += y_max - y_min + 1
    
#     return total


def rectangle_rotation(a, b):
    a //= 2**0.5
    b //= 2**0.5
    r = (a + 1) * (b + 1) + a * b

    return r + r % 2 - 1

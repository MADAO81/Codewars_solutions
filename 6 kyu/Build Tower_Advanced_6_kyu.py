# https://www.codewars.com/kata/57675f3dedc6f728ee000256/train/python

def tower_builder(n_floors, block_size):
    w, h = block_size
    max_width = n_floors * w * 2 - w
    return [
        ('*' * ((i + 1) * w * 2 - w)).center(max_width)
        for i in range(n_floors)
        for _ in range(h)
    ]

# https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python

import math

class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.sqrt_n = int(math.sqrt(self.n))
    
    def is_valid(self):
        if (self.n == 0 or self.sqrt_n ** 2 != self.n or 
            any(len(row) != self.n for row in self.data) or
            any(not isinstance(num, int) for row in self.data for num in row)):
            return False
        
        def valid_group(group):
            return sorted(group) == list(range(1, self.n + 1))
        
        for row in self.data:
            if not valid_group(row):
                return False
        
        for j in range(self.n):
            if not valid_group([self.data[i][j] for i in range(self.n)]):
                return False
        
        for br in range(self.sqrt_n):
            for bc in range(self.sqrt_n):
                box = [self.data[br * self.sqrt_n + i][bc * self.sqrt_n + j] 
                       for i in range(self.sqrt_n) for j in range(self.sqrt_n)]
                if not valid_group(box):
                    return False

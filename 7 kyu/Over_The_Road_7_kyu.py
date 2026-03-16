# https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/python

# if your house is [even/odd], the opposite house will be [odd/even] 
# highest number on street is 2n 
# Left side houses are [1, 3, ... 2n-3, 2n-1] 
# Right side houses are [2n, 2n-2, ... 4, 2] 
# Sum of opposite house numbers will always be 2n+1 

def over_the_road(address, n):
    return n*2-address+1

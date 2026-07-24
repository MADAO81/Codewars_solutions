# https://www.codewars.com/kata/55c4eb777e07c13528000021/train/python

def zeroes(base, number):
    factors = {}
    d = 2
    while d*d <= base:
        while base % d == 0:
            factors[d] = factors.get(d,0) + 1
            base //=d
        d += 1 if d == 2 else 2
    if base > 1:
        factors[base] = factors.get(base, 0) + 1
        
    return min(sum(number // (p ** i) for  i in range(1,100) if p ** i <= number) // exp for p, exp in factors.items())

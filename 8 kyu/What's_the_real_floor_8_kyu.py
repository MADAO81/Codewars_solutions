What's the real floor

def get_real_floor(n):
    if n <= 0:
        return n
    if 1 <= n < 13:
        return abs(n) - 1
    else:
        return abs(n) - 2

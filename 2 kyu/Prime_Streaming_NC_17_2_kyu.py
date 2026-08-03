# https://www.codewars.com/kata/59122604e5bc240817000016/train/python

def primes():
    yield 2
    sieve = {}
    n = 3
    while True:
        if n not in sieve:
            yield n
            sieve[n * n] = 2 * n
        else:
            step = sieve[n]
            next_mult = n + step
            while next_mult in sieve:
                next_mult += step
            sieve[next_mult] = step
            del sieve[n]
        n += 2

# https://www.codewars.com/kata/59122604e5bc240817000016/train/python

def primes():
    yield 2
    
    # Размер блока — 1 миллион чисел за раз
    BLOCK = 1 << 20
    
    # Начальные простые числа до 1000 (для начала)
    limit = 1000
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = b'\x00' * (((limit - i*i) // i) + 1)
    
    base_primes = [i for i in range(2, limit + 1) if sieve[i]]
    
    # Выдаем все простые до 1000
    for p in base_primes:
        if p > 2:
            yield p
    
    start = limit + 1
    
    while True:
        segment = bytearray(b'\x01') * BLOCK
        segment_start = start
        segment_end = start + BLOCK
        
        # Обновляем базовые простые числа до sqrt(segment_end)
        sqrt_limit = int(segment_end ** 0.5) + 1
        while base_primes[-1] <= sqrt_limit:
            n = base_primes[-1] + 2
            while True:
                is_prime = True
                for p in base_primes:
                    if p * p > n:
                        break
                    if n % p == 0:
                        is_prime = False
                        break
                if is_prime:
                    base_primes.append(n)
                    break
                n += 2
        
        # Отмечаем составные числа в сегменте
        for p in base_primes:
            if p > sqrt_limit:
                break
            
            # Первое кратное p в сегменте
            first = max(p * p, ((segment_start + p - 1) // p) * p)
            
            # Делаем нечетным (если p != 2)
            if p != 2 and first % 2 == 0:
                first += p
            
            # Отмечаем все кратные
            step = p if p == 2 else p * 2
            for j in range(first, segment_end, step):
                segment[j - segment_start] = 0
        
        # Выдаем простые числа из сегмента
        for i in range(segment_start, segment_end):
            if segment[i - segment_start]:
                yield i
        
        start = segment_end

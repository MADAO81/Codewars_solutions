# Your task is to create a function that returns true if the given number is a Wilson prime and false otherwise.

def am_i_wilson(n):
    wilson_primes = [5,13,563]
    return n in wilson_primes

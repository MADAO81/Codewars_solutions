# Count the Monkeys!
# You take your son to the forest to see the monkeys. 
# ou know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

# For example(Input --> Output):

# 10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  1 --> [1]

# def monkey_count(n):
#     monkeys = []
#     count = 1
#     while count <= n:
#         monkeys.append(count)
#         count +=1
#     return monkeys
    
monkey_count=lambda n:[m for m in range(1,n+1)]

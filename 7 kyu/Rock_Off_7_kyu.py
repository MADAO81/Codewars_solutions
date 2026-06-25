# https://www.codewars.com/kata/5b097da6c3323ac067000036/train/python


# def solve(a, b):
#     mesg = ['Alice made "Kurt" proud!', 'that looks like a "draw"! Rock on!', 'Bob made "Jeff" proud!']
#     alice, bob = sum(x>y for x,y in zip(a,b)), sum(x<y for x,y in zip(a,b))
#     return f'{alice}, {bob}: {mesg[(bob >= alice) + (bob > alice)]}'



def solve(a, b):
    alice = sum(i > j for i, j in zip(a, b))
    bob = sum(j > i for i, j in zip(a, b))
    
    if alice == bob:
        words = 'that looks like a "draw"! Rock on!'
    elif alice > bob:
        words = 'Alice made "Kurt" proud!'
    else:
        words = 'Bob made "Jeff" proud!'
    
    return '{}, {}: {}'.format(alice, bob, words) 

# https://www.codewars.com/kata/5982619d2671576e90000017/train/python

def sponge_meme( s ):
    return "".join([char.upper() if i%2 ==0 else char.lower() for i,char in enumerate(s)])

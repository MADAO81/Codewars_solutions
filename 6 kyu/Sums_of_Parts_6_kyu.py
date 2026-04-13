# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python

def parts_sums(ls):
    result = [sum(ls)]
    for i in ls:
        result.append(result[-1]-i)
    return result

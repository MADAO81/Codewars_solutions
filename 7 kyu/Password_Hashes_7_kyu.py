# https://www.codewars.com/kata/54207f9677730acd490000d1/train/python

# import hashlib

# def pass_hash(str):
#     result = hashlib.md5(str.encode('utf-8'))
#     return result.hexdigest()


from hashlib import md5

def pass_hash(str):
    return md5(str.encode()).hexdigest()

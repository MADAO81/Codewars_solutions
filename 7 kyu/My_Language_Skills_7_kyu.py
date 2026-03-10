# https://www.codewars.com/kata/5b16490986b6d336c900007d/train/python

def my_languages(results):
    return sorted([k for k,v in results.items() if v >=60], key = lambda x:results[x], reverse = True)

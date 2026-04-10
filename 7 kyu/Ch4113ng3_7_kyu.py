# https://www.codewars.com/kata/59e9f404fc3c49ab24000112/train/python

# def nerdify(txt):
#     table = str.maketrans('aAeEl','44331')
#     return txt.translate(table)

def nerdify(txt):
    return txt.translate(str.maketrans("aAeEl", "44331"))

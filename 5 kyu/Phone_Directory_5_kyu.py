# https://www.codewars.com/kata/56baeae7022c16dd7400086e/train/python

# import re
# def phone(strng, num):
#     if strng.count('+'+num) == 0:
#         errormsg = 'Error => Not found: '+num
#         return errormsg
#     elif strng.count('+'+num) > 1:
#         errormsg = 'Error => Too many people: '+num
#         return errormsg
#     else:
#         strng = re.sub(r'[;:,\/_\?!\$*]', r' ', strng)
#         lst = strng.split('\n')
#         nameregex = re.compile(r'<([\w\s\']+)>')
#         for i in range(len(lst)):
#             if '+'+num in lst[i]:
#                 name = nameregex.search(lst[i])
#                 adress = lst[i].replace('+'+num, '').replace(name.group(), '')
#     adresslist = adress.split()
#     adress = ' '.join(adresslist)
#     returnString = "Phone => "+num+", Name => "+name.group(1)+", Address => "+adress
#     return returnString


from re import sub

def phone(dir, num):
    if dir.count("+" + num) == 0:
        return "Error => Not found: " + num
    
    if dir.count("+" + num) > 1:
        return "Error => Too many people: " + num
    
    for line in dir.splitlines():
        if "+" + num in line:
            name = sub(".*<(.*)>.*", "\g<1>", line)
            line = sub("<" + name + ">|\+" + num, "", line)
            address = " ".join(sub("[^a-zA-Z0-9\.-]", " ", line).split())
            return "Phone => %s, Name => %s, Address => %s" % (num, name, address)

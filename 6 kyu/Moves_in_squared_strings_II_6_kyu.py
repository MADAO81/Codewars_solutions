# https://www.codewars.com/kata/56dbe7f113c2f63570000b86/train/python

# def rot(strng):
#     return strng[::-1]
# def selfie_and_rot(strng):
#     return '\n'.join(i+'.'*len(i) for i in strng.split('\n')) + '\n' +'\n'.join('.'*len(i)+i[::-1] for i in strng.split('\n')[::-1])
# def oper(fct, s):
#     return fct(s)


def rot(string):
    return string[::-1]

def selfie_and_rot(string):
    s_dot = '\n'.join([ s+'.'*len(s) for s in string.split('\n') ])   
    return s_dot+'\n'+rot(s_dot)

def oper(fct, s):
    return fct(s)

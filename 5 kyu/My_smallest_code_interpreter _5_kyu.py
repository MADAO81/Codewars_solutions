# https://www.codewars.com/kata/526156943dfe7ce06200063e/train/python


from collections import defaultdict

def brain_luck(code, input):
    p, i = 0, 0
    output = []
    input = iter(input)
    data = defaultdict(int)
    while i < len(code):
        c = code[i]
        if c == '+': 
            data[p] = (data[p] + 1) % 256
        elif c == '-': 
            data[p] = (data[p] - 1) % 256
        elif c == '>': 
            p += 1
        elif c == '<': 
            p -= 1
        elif c == '.': 
            output.append(chr(data[p]))
        elif c == ',': 
            data[p] = ord(next(input))
        elif c == '[':
            if not data[p]:
                depth = 1
                while depth > 0:
                    i += 1
                    c = code[i]
                    if c == '[': 
                        depth += 1
                    elif c== ']': 
                        depth -= 1
        elif c == ']':
            if data[p]:
                depth = 1
                while depth > 0:
                    i -= 1
                    c = code[i]
                    if c == ']': 
                        depth += 1
                    elif c == '[': 
                        depth -= 1
        i += 1
    return ''.join(output)

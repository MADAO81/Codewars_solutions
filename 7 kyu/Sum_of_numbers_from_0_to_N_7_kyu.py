# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python

# def show_sequence(n):
#     if n == 0:
#         return "0=0"
#     elif n < 0:
#         return str(n) + "<0"
#     else:
#         counter = sum(range(n+1))
#         return '+'.join(map(str, range(n+1))) + " = " + str(counter)

def show_sequence(n):
    if n == 0:
        return f"{n}=0"
    elif n < 0:
        return f"{n}<0"
    else:
        result = sum(range(n+1))
        result_str = "+".join(map(str,range(n+1)))
        return f"{result_str} = {result}"
        

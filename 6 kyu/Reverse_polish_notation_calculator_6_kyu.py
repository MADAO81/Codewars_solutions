# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

# For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

# For your convenience, the input is formatted such that a space is provided between every token.

# Empty expression should evaluate to 0.

# Valid operations are +, -, *, /.

# You may assume that there won't be exceptional situations (like stack underflow or division by zero).


# def calc(expr):
#     expr = expr.split(" ") if expr else "0"
#     result = []
#     for i in range(len(expr)):
#         if not expr[i] in "+*/-":
#             result.append(expr[i])
#         else:
#             result.append(f"({result.pop(-2)} {expr[i]} {result.pop()})")
#     answer = eval(result.pop()) if result else eval(expr)
#     return int(answer) if not answer % 2 else answer




# operator = set(['+', '-', '*', '/'])

# def calc(expr):
#     stack = list()
#     for c in expr.split():
#     	if c in operator : 
#         	first = stack.pop()
#         	second = stack.pop()
#         	stack.append(str(eval(second + c + first)))
#         else : stack.append(c)
#     return eval(stack.pop()) if stack else 0
  

import operator

def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1,op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

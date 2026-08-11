# https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python

def interpret(code):
    # Split code into grid
    lines = code.split('\n')
    height = len(lines)
    width = max(len(line) for line in lines)
    
    # Pad all lines to same width
    grid = [list(line.ljust(width)) for line in lines]
    
    # Initialize interpreter state
    stack = []
    output = ""
    x, y = 0, 0  # Starting position
    dx, dy = 1, 0  # Starting direction (right)
    string_mode = False
    
    # Directions mapping
    directions = {
        '>': (1, 0),
        '<': (-1, 0),
        '^': (0, -1),
        'v': (0, 1)
    }
    
    while True:
        char = grid[y][x]
        
        # String mode
        if string_mode and char != '"':
            stack.append(ord(char))
            x = (x + dx) % width
            y = (y + dy) % height
            continue
        elif char == '"':
            string_mode = not string_mode
            x = (x + dx) % width
            y = (y + dy) % height
            continue
        
        # Handle all other instructions
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            a = stack.pop() if stack else 0
            b = stack.pop() if stack else 0
            stack.append(b + a)
        elif char == '-':
            a = stack.pop() if stack else 0
            b = stack.pop() if stack else 0
            stack.append(b - a)
        elif char == '*':
            a = stack.pop() if stack else 0
            b = stack.pop() if stack else 0
            stack.append(b * a)
        elif char == '/':
            a = stack.pop() if stack else 0
            b = stack.pop() if stack else 0
            stack.append(b // a if a != 0 else 0)
        elif char == '%':
            a = stack.pop() if stack else 0
            b = stack.pop() if stack else 0
            stack.append(b % a if a != 0 else 0)
        elif char == '!':
            a = stack.pop() if stack else 0
            stack.append(1 if a == 0 else 0)
        elif char == '`':
            a = stack.pop() if stack else 0
            b = stack.pop() if stack else 0
            stack.append(1 if b > a else 0)
        elif char in directions:
            dx, dy = directions[char]
        elif char == '?':
            import random
            directions_list = [(1,0), (-1,0), (0,-1), (0,1)]
            dx, dy = random.choice(directions_list)
        elif char == '_':
            a = stack.pop() if stack else 0
            dx = 1 if a == 0 else -1
            dy = 0
        elif char == '|':
            a = stack.pop() if stack else 0
            dx = 0
            dy = 1 if a == 0 else -1
        elif char == ':':
            if stack:
                stack.append(stack[-1])
            else:
                stack.append(0)
        elif char == '\\':
            if len(stack) >= 2:
                stack[-1], stack[-2] = stack[-2], stack[-1]
            elif len(stack) == 1:
                stack.append(0)
                stack[-1], stack[-2] = stack[-2], stack[-1]
            else:
                stack.append(0)
                stack.append(0)
        elif char == '$':
            if stack:
                stack.pop()
        elif char == '.':
            if stack:
                output += str(stack.pop())
        elif char == ',':
            if stack:
                output += chr(stack.pop())
        elif char == '#':
            # Trampoline: skip next cell
            x = (x + dx) % width
            y = (y + dy) % height
        elif char == 'p':
            y_pos = stack.pop() if stack else 0
            x_pos = stack.pop() if stack else 0
            v = stack.pop() if stack else 0
            if 0 <= y_pos < height and 0 <= x_pos < width:
                grid[y_pos][x_pos] = chr(v)
        elif char == 'g':
            y_pos = stack.pop() if stack else 0
            x_pos = stack.pop() if stack else 0
            if 0 <= y_pos < height and 0 <= x_pos < width:
                stack.append(ord(grid[y_pos][x_pos]))
            else:
                stack.append(0)
        elif char == '@':
            break
        # Space is no-op, do nothing
        
        # Move to next cell
        x = (x + dx) % width
        y = (y + dy) % height
    
    return output

# https://www.codewars.com/kata/5868a68ba44cfc763e00008d/train/python


def interpreter(code, iterations, width, height):
    # Инициализация сетки
    grid = [[0] * width for _ in range(height)]
    
    # Позиция указателя (строка, колонка)
    row, col = 0, 0
    
    # Сопоставление скобок
    bracket_map = {}
    stack = []
    for i, char in enumerate(code):
        if char == '[':
            stack.append(i)
        elif char == ']':
            if stack:
                start = stack.pop()
                bracket_map[start] = i
                bracket_map[i] = start
    
    # Выполнение кода
    i = 0
    iterations_done = 0
    
    while i < len(code) and iterations_done < iterations:
        command = code[i]
        
        if command == 'n':
            row = (row - 1) % height
            iterations_done += 1
        elif command == 'e':
            col = (col + 1) % width
            iterations_done += 1
        elif command == 's':
            row = (row + 1) % height
            iterations_done += 1
        elif command == 'w':
            col = (col - 1) % width
            iterations_done += 1
        elif command == '*':
            grid[row][col] = 1 - grid[row][col]
            iterations_done += 1
        elif command == '[':
            if grid[row][col] == 0:
                i = bracket_map[i]
            iterations_done += 1
        elif command == ']':
            if grid[row][col] != 0:
                i = bracket_map[i]
            iterations_done += 1
        # Остальные символы игнорируем
        
        i += 1
    
    # Формирование результата
    return '\r\n'.join(''.join(str(cell) for cell in row) for row in grid)

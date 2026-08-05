# https://www.codewars.com/kata/5671d975d81d6c1c87000022/train/python

# def solve_puzzle(clues):
#     # Переводим индексы подсказок в координаты строк/столбцов и направлений
#     # 0-3: верх (сверху вниз), 4-7: право (слева направо)
#     # 8-11: низ (снизу вверх), 12-15: лево (снизу вверх)
    
#     def get_row_clues(row):
#         # Подсказки для строки: слева и справа
#         left = clues[15 - row]  # левая сторона, индекс 15,14,13,12
#         right = clues[4 + row]  # правая сторона, индекс 4,5,6,7
#         return left, right
    
#     def get_col_clues(col):
#         # Подсказки для столбца: сверху и снизу
#         top = clues[col]  # верх, индекс 0,1,2,3
#         bottom = clues[11 - col]  # низ, индекс 11,10,9,8
#         return top, bottom
    
#     def count_visible(line):
#         # Подсчет видимых зданий в линии
#         visible = 0
#         max_height = 0
#         for height in line:
#             if height > max_height:
#                 visible += 1
#                 max_height = height
#         return visible
    
#     def check_clues():
#         # Проверка всех подсказок
#         # Проверяем строки
#         for row in range(4):
#             left, right = get_row_clues(row)
#             if left and count_visible(grid[row]) != left:
#                 return False
#             if right and count_visible(grid[row][::-1]) != right:
#                 return False
        
#         # Проверяем столбцы
#         for col in range(4):
#             column = [grid[row][col] for row in range(4)]
#             top, bottom = get_col_clues(col)
#             if top and count_visible(column) != top:
#                 return False
#             if bottom and count_visible(column[::-1]) != bottom:
#                 return False
        
#         return True
    
#     def is_valid(row, col, num):
#         # Проверка, можно ли поставить num в позицию (row, col)
#         # Проверяем строку
#         if num in grid[row]:
#             return False
        
#         # Проверяем столбец
#         for r in range(4):
#             if grid[r][col] == num:
#                 return False
        
#         return True
    
#     def backtrack(row, col):
#         if row == 4:
#             # Все ячейки заполнены
#             return check_clues()
        
#         # Переходим к следующей ячейке
#         next_row = row if col < 3 else row + 1
#         next_col = (col + 1) % 4
        
#         # Пробуем все возможные значения (1-4)
#         for num in range(1, 5):
#             if is_valid(row, col, num):
#                 grid[row][col] = num
                
#                 # Оптимизация: проверяем частичные подсказки
#                 # Проверяем завершенные строки
#                 if col == 3:
#                     left, right = get_row_clues(row)
#                     if left and count_visible(grid[row]) != left:
#                         grid[row][col] = 0
#                         continue
#                     if right and count_visible(grid[row][::-1]) != right:
#                         grid[row][col] = 0
#                         continue
                
#                 # Проверяем завершенные столбцы
#                 if row == 3:
#                     column = [grid[r][col] for r in range(4)]
#                     top, bottom = get_col_clues(col)
#                     if top and count_visible(column) != top:
#                         grid[row][col] = 0
#                         continue
#                     if bottom and count_visible(column[::-1]) != bottom:
#                         grid[row][col] = 0
#                         continue
                
#                 if backtrack(next_row, next_col):
#                     return True
                
#                 grid[row][col] = 0  # откат
        
#         return False
    
#     # Инициализация сетки
#     grid = [[0] * 4 for _ in range(4)]
    
#     # Запуск поиска
#     backtrack(0, 0)
    
#     # Преобразуем в tuple of tuples
#     return tuple(tuple(row) for row in grid)



def solve_puzzle(clues):
    # Convert clue indices to row/column coordinates and directions
    # 0-3: top (top to bottom), 4-7: right (left to right)
    # 8-11: bottom (bottom to top), 12-15: left (bottom to top)
    
    def get_row_clues(row):
        # Get left and right clues for a specific row
        left = clues[15 - row]  # left side, indices 15,14,13,12
        right = clues[4 + row]  # right side, indices 4,5,6,7
        return left, right
    
    def get_col_clues(col):
        # Get top and bottom clues for a specific column
        top = clues[col]  # top side, indices 0,1,2,3
        bottom = clues[11 - col]  # bottom side, indices 11,10,9,8
        return top, bottom
    
    def count_visible(line):
        # Count how many buildings are visible from one side
        # A building is visible if it's taller than all previous buildings
        visible = 0
        max_height = 0
        for height in line:
            if height > max_height:
                visible += 1
                max_height = height
        return visible
    
    def check_clues():
        # Verify all clues after the grid is completely filled
        
        # Check all rows
        for row in range(4):
            left, right = get_row_clues(row)
            if left and count_visible(grid[row]) != left:
                return False
            if right and count_visible(grid[row][::-1]) != right:
                return False
        
        # Check all columns
        for col in range(4):
            column = [grid[row][col] for row in range(4)]
            top, bottom = get_col_clues(col)
            if top and count_visible(column) != top:
                return False
            if bottom and count_visible(column[::-1]) != bottom:
                return False
        
        return True
    
    def is_valid(row, col, num):
        # Check if placing 'num' at position (row, col) is valid
        
        # Check if 'num' already exists in the current row
        if num in grid[row]:
            return False
        
        # Check if 'num' already exists in the current column
        for r in range(4):
            if grid[r][col] == num:
                return False
        
        return True
    
    def backtrack(row, col):
        # Recursive backtracking function to fill the grid
        
        # Base case: all cells are filled
        if row == 4:
            return check_clues()
        
        # Calculate next cell position (row-major order)
        next_row = row if col < 3 else row + 1
        next_col = (col + 1) % 4
        
        # Try all possible values (1 to 4) for the current cell
        for num in range(1, 5):
            if is_valid(row, col, num):
                # Place the number
                grid[row][col] = num
                
                # Optimization: Check partially completed rows
                if col == 3:
                    left, right = get_row_clues(row)
                    # If left clue exists and doesn't match, backtrack
                    if left and count_visible(grid[row]) != left:
                        grid[row][col] = 0
                        continue
                    # If right clue exists and doesn't match, backtrack
                    if right and count_visible(grid[row][::-1]) != right:
                        grid[row][col] = 0
                        continue
                
                # Optimization: Check partially completed columns
                if row == 3:
                    column = [grid[r][col] for r in range(4)]
                    top, bottom = get_col_clues(col)
                    # If top clue exists and doesn't match, backtrack
                    if top and count_visible(column) != top:
                        grid[row][col] = 0
                        continue
                    # If bottom clue exists and doesn't match, backtrack
                    if bottom and count_visible(column[::-1]) != bottom:
                        grid[row][col] = 0
                        continue
                
                # Recursively fill the rest of the grid
                if backtrack(next_row, next_col):
                    return True
                
                # Backtrack: undo the placement
                grid[row][col] = 0
        
        # No valid number found for this cell
        return False
    
    # Initialize empty 4x4 grid
    grid = [[0] * 4 for _ in range(4)]
    
    # Start the backtracking search from the top-left corner
    backtrack(0, 0)
    
    # Convert to tuple of tuples as required by the problem statement
    return tuple(tuple(row) for row in grid)



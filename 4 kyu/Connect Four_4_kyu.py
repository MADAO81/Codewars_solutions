# https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python

def who_is_winner(pieces_position_list):
    # Создаем игровое поле 6x7 (строки 0-5, столбцы 0-6)
    # Будем хранить цвета в виде строк: "R" или "Y"
    board = [['' for _ in range(7)] for _ in range(6)]
    
    # Словарь для перевода букв столбцов в индексы
    col_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    
    # Текущая высота (количество фигур) в каждом столбце
    heights = [0] * 7
    
    def check_winner(row, col, color):
        """Проверяет, есть ли 4 в ряд начиная с позиции (row, col)"""
        
        # Проверяем все 4 направления: горизонталь, вертикаль, диагональ \ и /
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        
        for dr, dc in directions:
            count = 1  # Учитываем текущую клетку
            
            # Проверяем в положительном направлении
            r, c = row + dr, col + dc
            while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == color:
                count += 1
                r += dr
                c += dc
            
            # Проверяем в отрицательном направлении
            r, c = row - dr, col - dc
            while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == color:
                count += 1
                r -= dr
                c -= dc
            
            if count >= 4:
                return True
        
        return False
    
    # Обрабатываем ходы
    for move in pieces_position_list:
        col_letter, color_full = move.split('_')
        col = col_to_index[col_letter]
        color = 'R' if color_full == 'Red' else 'Y'
        
        # Находим строку, куда упадет фигура
        row = heights[col]
        
        # Проверяем, что столбец не переполнен
        if row >= 6:
            continue
            
        # Ставим фигуру
        board[row][col] = color
        heights[col] += 1
        
        # Проверяем, есть ли победитель
        if check_winner(row, col, color):
            return color_full
    
    # Если никто не выиграл за 42 хода
    return "Draw"

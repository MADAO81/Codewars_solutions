# https://www.codewars.com/kata/585894545a8a07255e0002f1/train/python

def count_patterns_from(firstPoint, length):
    # Проверка на валидность входных данных
    if length <= 0 or length > 9:
        return 0
    
    # Маппинг точек к индексам (0-8)
    points = 'ABCDEFGHI'
    start = points.index(firstPoint)
    
    # Предварительно вычисляем, какие точки лежат между каждой парой
    jumps = [[-1]*9 for _ in range(9)]
    
    # Заполняем jumps для всех пар, где есть промежуточная точка
    # Горизонтальные линии
    jumps[0][2] = jumps[2][0] = 1  # A-C через B
    jumps[3][5] = jumps[5][3] = 4  # D-F через E
    jumps[6][8] = jumps[8][6] = 7  # G-I через H
    
    # Вертикальные линии
    jumps[0][6] = jumps[6][0] = 3  # A-G через D
    jumps[1][7] = jumps[7][1] = 4  # B-H через E
    jumps[2][8] = jumps[8][2] = 5  # C-I через F
    
    # Диагонали
    jumps[0][8] = jumps[8][0] = 4  # A-I через E
    jumps[2][6] = jumps[6][2] = 4  # C-G через E
    
    visited = [False]*9
    visited[start] = True
    
    def dfs(current, remaining):
        if remaining == 0:
            return 1
        
        total = 0
        for next_point in range(9):
            if visited[next_point]:
                continue
            
            jump = jumps[current][next_point]
            # Если есть промежуточная точка, проверяем, использована ли она
            if jump != -1 and not visited[jump]:
                continue
            
            visited[next_point] = True
            total += dfs(next_point, remaining - 1)
            visited[next_point] = False
        
        return total
    
    return dfs(start, length - 1)

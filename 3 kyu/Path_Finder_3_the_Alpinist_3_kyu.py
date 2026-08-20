# https://www.codewars.com/kata/576986639772456f6f00030c/train/python

import heapq

def path_finder(area):
    # Преобразуем строку в матрицу чисел
    grid = [[int(c) for c in row] for row in area.split('\n')]
    n = len(grid)
    
    # Расстояния до каждой клетки
    distances = [[float('inf')] * n for _ in range(n)]
    distances[0][0] = 0
    
    # Очередь с приоритетом: (расстояние, x, y)
    heap = [(0, 0, 0)]
    
    # Направления движения: вверх, вниз, влево, вправо
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while heap:
        dist, x, y = heapq.heappop(heap)
        
        # Если достигли цели
        if x == n - 1 and y == n - 1:
            return dist
        
        # Если нашли более короткий путь к этой клетке
        if dist > distances[x][y]:
            continue
        
        # Пробуем все направления
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Проверяем границы
            if 0 <= nx < n and 0 <= ny < n:
                # Вычисляем разницу высот
                climb = abs(grid[nx][ny] - grid[x][y])
                new_dist = dist + climb
                
                # Если нашли более короткий путь
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(heap, (new_dist, nx, ny))
    
    return distances[n - 1][n - 1]

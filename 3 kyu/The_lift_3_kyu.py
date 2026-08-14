# https://www.codewars.com/kata/58905bfa1decb981da00009e/train/python


cclass Dinglemouse(object):

    def __init__(self, queues, capacity):
        # Создаем две структуры очередей: для движения вверх ('U') и вниз ('D')
        # Для каждого этажа (i) и каждой очереди (q) оставляем только тех,
        # кто хочет ехать в соответствующем направлении
        # [::-1] разворачивает очередь, чтобы pop() брал первого в очереди
        self.Q = {
            k: [
                [p for p in q if (p > i if k == 'U' else p < i)][::-1]
                for i, q in enumerate(queues)
            ]
            for k in 'UD'
        }
        
        # Список всех этажей для проверки границ
        self.floors = [f for f in range(len(queues))]
        self.capacity = capacity

    def theLift(self):
        # Текущий этаж, направление, пассажиры в лифте, маршрут
        f, d, lift, path = 0, 'U', [], [0]
        
        # Пока есть люди в очередях или в лифте
        while sum(len(q) for q in self.Q['U']) + sum(len(q) for q in self.Q['D']) + len(lift) > 0:
            
            # Проверяем, нужно ли остановиться на текущем этаже:
            # - есть ли кто-то, кто хочет сесть в текущем направлении (self.Q[d][f])
            # - есть ли пассажиры, которые хотят выйти (f in lift)
            if self.Q[d][f] or f in lift:
                # Записываем остановку, если это не дубликат
                if path[-1] != f:
                    path.append(f)
                
                # ВЫСАДКА: удаляем всех пассажиров, кто хотел выйти на этом этаже
                lift = [p for p in lift if p != f]
                
                # ПОСАДКА: пока есть место и есть люди в очереди
                while len(lift) < self.capacity and self.Q[d][f]:
                    # pop() берет последнего в очереди
                    # благодаря [::-1] в __init__, это будет первый в очереди
                    lift.append(self.Q[d][f].pop())

            # ДВИЖЕНИЕ: делаем шаг в текущем направлении
            f += {'U': 1, 'D': -1}[d]
            
            # Если вышли за пределы здания
            if f not in self.floors:
                # Разворачиваемся
                d = {'U': 'D', 'D': 'U'}[d]
                # Делаем шаг в новом направлении (возвращаемся в здание)
                f += {'U': 1, 'D': -1}[d]
                    
        # Если последняя остановка не на 0 этаже - возвращаемся
        return path if path[-1] == 0 else path + [0]

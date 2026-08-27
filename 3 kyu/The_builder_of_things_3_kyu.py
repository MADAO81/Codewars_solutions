# https://www.codewars.com/kata/5571d9fc11526780a000011a/train/python

from functools import partial

class Proxy:
    """
    Прокси-класс для перехвата атрибутов и создания цепочек.
    Позволяет обрабатывать вызовы вида is_a.woman, is_the.parent_of.joe и т.д.
    """
    def __init__(self, get):
        self.get = get  # Функция, которая будет вызвана при обращении к атрибуту
    
    def __getattr__(self, name):
        # Вызываем функцию с именем атрибута
        result = self.get(name)
        if result is not None:
            return result
        # Если результат None, возвращаем сам прокси для продолжения цепочки
        return self


class Thing:
    def __init__(self, name):
        self.name = name
        self._props = {}         # Словарь для хранения свойств (parent_of -> 'joe')
        self._children = []      # Список дочерних элементов (для has(n))
        self._methods = {}       # Словарь методов (speak, flex и т.д.)
        self._archives = {}      # Словарь для архивации результатов методов
        
        # Автоматически добавляем is_name свойство (например, is_Jane)
        setattr(self, f'is_{name}', True)
        
        # Цепочка is_a.woman -> создает is_a_woman = True
        self.is_a = Proxy(lambda s: setattr(self, f'is_a_{s}', True) or self)
        
        # Цепочка is_not_a.man -> создает is_a_man = False
        self.is_not_a = Proxy(lambda s: setattr(self, f'is_a_{s}', False) or self)
        
        # Цепочка is_the.parent_of.joe -> устанавливает свойство parent_of = 'joe'
        # being_the и and_the работают аналогично
        self.is_the = self.being_the = self.and_the = Proxy(
            lambda k: Proxy(lambda v: self._set_prop(k, v) or self)
        )
        
        # Цепочка can.speak(method) -> добавляет метод speak
        self.can = Proxy(lambda s: partial(self._add_method, s))
        
        # Цепочка has(n).property -> создает n дочерних элементов
        self.has = self.having = lambda n: Proxy(lambda s: self._add_child(n, s))
    
    def _set_prop(self, key, value):
        """Устанавливает свойство (используется для is_the.parent_of.joe)"""
        self._props[key] = value
        return self
    
    def _add_child(self, n, name):
        """Создает дочерний элемент для has(n).property"""
        t = Thing(name) if n == 1 else Things(n, name)
        self._props[name] = t
        return t
    
    def _add_method(self, name, method, archive=None):
        """Добавляет метод через can.verb(method, archive)"""
        if archive:
            # Если указан archive, сохраняем результаты
            saved = []
            self._archives[archive] = saved
            method = self._save_to(method, saved)
        # Привязываем метод к экземпляру
        self._methods[name] = method.__get__(self, Thing)
        return self
    
    @staticmethod
    def _save_to(func, saved):
        """Обертка для сохранения результатов метода в архив"""
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            saved.append(result)
            return result
        return wrapper
    
    def __getattr__(self, name):
        """Перехватывает обращение к отсутствующим атрибутам"""
        
        # Проверяем is_* свойства (которые не были созданы через is_a)
        if name.startswith('is_'):
            prop = name[3:]
            # Проверяем, есть ли такое свойство в _props
            if prop in self._props:
                return True
            # Или проверяем, не является ли это именем самого объекта
            if prop == self.name:
                return True
            return False
        
        # Проверяем существующие свойства
        if name in self._props:
            return self._props[name]
        
        # Проверяем архивы
        if name in self._archives:
            return self._archives[name]
        
        # Проверяем методы
        if name in self._methods:
            return self._methods[name]
        
        # Если ничего не найдено, создаем новое свойство
        thing = Thing(name)
        self._props[name] = thing
        return thing
    
    def __len__(self):
        """Поддерживает len() для объектов с дочерними элементами"""
        return len(self._children)
    
    def __getitem__(self, index):
        """Поддерживает индексацию для доступа к дочерним элементам"""
        if isinstance(index, int) and 0 <= index < len(self._children):
            return self._children[index]
        raise IndexError("Index out of range")
    
    def __iter__(self):
        """Поддерживает итерацию по дочерним элементам"""
        return iter(self._children)
    
    def __repr__(self):
        return f"Thing('{self.name}')" if self.name else "Thing()"


class Things(Thing, list):
    """
    Класс для хранения нескольких дочерних элементов.
    Наследует от Thing (для поддержки методов) и list (для итерации)
    """
    def __init__(self, n, name):
        Thing.__init__(self, name)
        # Убираем 's' на конце для получения единственного числа
        single = name.removesuffix('s') if name.endswith('s') else name
        # Создаем n дочерних элементов с именами single_1, single_2, ...
        self._children = [Thing(single) for _ in range(n)]
        # Инициализируем list для поддержки итерации и индексации
        list.__init__(self, self._children)
    
    def each(self, func):
        """Применяет функцию к каждому дочернему элементу"""
        for it in self:
            func(it)
        return self

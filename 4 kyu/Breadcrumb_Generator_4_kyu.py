# https://www.codewars.com/kata/563fbac924106b8bf7000046/train/python


# def generate_bc(url, separator):
#     # Игнорируем якоря и параметры
#     url = url.split('#')[0].split('?')[0]
    
#     # Удаляем протокол (http://, https://)
#     if '://' in url:
#         url = url.split('://')[1]
    
#     # Разделяем на домен и путь
#     parts = url.split('/')
    
#     # Получаем путь (все, что после домена)
#     path_parts = parts[1:] if len(parts) > 1 else []
    
#     # Удаляем пустые элементы
#     path_parts = [p for p in path_parts if p]
    
#     # Если путь пустой
#     if not path_parts:
#         return '<span class="active">HOME</span>'
    
#     # Очищаем путь от расширений и index
#     cleaned_path = []
    
#     for part in path_parts:
#         # Удаляем расширения
#         clean_part = part
#         for ext in ['.html', '.htm', '.php', '.asp']:
#             if clean_part.endswith(ext):
#                 clean_part = clean_part[:-len(ext)]
#                 break
        
#         # Если это index - пропускаем
#         if clean_part.lower() == 'index':
#             continue
        
#         cleaned_path.append(clean_part)
    
#     # Если после очистки путь пустой
#     if not cleaned_path:
#         return '<span class="active">HOME</span>'
    
#     # Строим хлебные крошки
#     elements = []
#     current_path = ''
    
#     # HOME - ссылка (если есть другие элементы)
#     elements.append('<a href="/">HOME</a>')
    
#     # Обрабатываем все элементы, кроме последнего
#     for i, part in enumerate(cleaned_path[:-1]):
#         if not part:
#             continue
#         current_path += '/' + part
#         name = format_name(part)
#         elements.append(f'<a href="{current_path}/">{name}</a>')
    
#     # Последний элемент - активный
#     if cleaned_path:
#         last_part = cleaned_path[-1]
#         if last_part:
#             name = format_name(last_part)
#             elements.append(f'<span class="active">{name}</span>')
    
#     return separator.join(elements)


# def format_name(name):
#     # Удаляем расширение если есть
#     for ext in ['.html', '.htm', '.php', '.asp']:
#         if name.endswith(ext):
#             name = name[:-len(ext)]
#             break
    
#     # Если имя пустое или index
#     if not name or name.lower() == 'index':
#         return ''
    
#     # Убираем дефисы и приводим к верхнему регистру
#     words = name.split('-')
    
#     # Проверяем длину
#     if len(name) > 30:
#         # Акронимизируем
#         ignore = {"the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"}
#         acronym = ''
#         for word in words:
#             if word.lower() not in ignore:
#                 acronym += word[0].upper()
#         return acronym
#     else:
#         # Просто заменяем дефисы на пробелы и приводим к верхнему регистру
#         return ' '.join(words).upper()


def generate_bc(url, separator):
    a, span = '<a href="%s/">%s</a>', '<span class="active">%s</span>'
    restricted = set("THE OF IN FROM BY WITH AND OR FOR TO AT A".split())
    
    def bc(menu):
        menu = menu.upper().replace('-', ' ')
        if len(menu) > 30: 
            menu = ''.join(w[0] for w in menu.split() if w not in restricted)
        return menu or 'HOME'
    
    # Обработка URL
    url = (''.join(url.strip('/').rpartition('//')[2].partition('/')[1:])
           .rsplit('?', 1)[0]
           .rsplit('#', 1)[0]
           .rsplit('.', 1)[0]
           .rsplit('/index')[0]
           .split('/'))
    
    # Если путь пустой
    if not url:
        return span % 'HOME'
    
    # Строим хлебные крошки
    breadcrumbs = []
    
    # Добавляем все элементы кроме последнего как ссылки
    for i, m in enumerate(url[:-1], 1):
        breadcrumbs.append(a % ('/'.join(url[:i]), bc(m)))
    
    # Добавляем последний элемент как активный
    breadcrumbs.append(span % bc(url[-1]))
    
    return separator.join(breadcrumbs)

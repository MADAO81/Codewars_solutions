# https://www.codewars.com/kata/5861487fdb20cff3ab000030/train/python

def boolfuck(code, input_=""):
    # Очищаем код от не-команд
    commands = [c for c in code if c in '+,;<[]>']
    
    # Подготовка памяти (бесконечная лента, начинаем с середины)
    tape = [0] * 100000
    pointer = 50000
    
    # Подготовка ввода (биты в little-endian порядке)
    input_bits = []
    for char in input_:
        # Получаем ASCII код символа и преобразуем в 8 бит (little-endian)
        bits = []
        n = ord(char)
        for i in range(8):
            bits.append((n >> i) & 1)
        input_bits.extend(bits)
    input_ptr = 0
    
    # Подготовка вывода (биты)
    output_bits = []
    
    # Подготовка для скобок
    bracket_map = {}
    stack = []
    
    for i, cmd in enumerate(commands):
        if cmd == '[':
            stack.append(i)
        elif cmd == ']':
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    
    # Выполнение программы
    i = 0
    while i < len(commands):
        cmd = commands[i]
        
        if cmd == '+':
            tape[pointer] ^= 1  # flip bit
        elif cmd == ',':
            if input_ptr < len(input_bits):
                tape[pointer] = input_bits[input_ptr]
                input_ptr += 1
            else:
                tape[pointer] = 0
        elif cmd == ';':
            output_bits.append(tape[pointer])
        elif cmd == '<':
            pointer -= 1
        elif cmd == '>':
            pointer += 1
        elif cmd == '[':
            if tape[pointer] == 0:
                i = bracket_map[i]
        elif cmd == ']':
            if tape[pointer] == 1:
                i = bracket_map[i]
        
        i += 1
    
    # Преобразование битов вывода в строку (little-endian, паддинг нулями)
    # Добавляем паддинг нулями до кратного 8
    while len(output_bits) % 8 != 0:
        output_bits.append(0)
    
    # Преобразуем биты в символы (группами по 8 бит)
    result = []
    for i in range(0, len(output_bits), 8):
        byte = 0
        for j in range(8):
            if output_bits[i + j] == 1:
                byte |= (1 << j)
        result.append(chr(byte))
    
    return ''.join(result)

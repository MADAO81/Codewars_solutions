# https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d/train/python

import heapq
from collections import Counter

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def is_leaf(self):
        return self.left is None and self.right is None

# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    if not s:
        return []
    freq_dict = Counter(s)
    return sorted([(char, freq) for char, freq in freq_dict.items()])

# Helper function to build Huffman tree
def build_tree(freqs):
    if not freqs or len(freqs) <= 1:
        return None
    
    heap = []
    for char, freq in freqs:
        heapq.heappush(heap, Node(freq, char))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, parent)
    
    return heap[0]

# Helper function to generate codes
def generate_codes(node, prefix="", code_map={}):
    if node.is_leaf():
        code_map[node.char] = prefix
    else:
        if node.left:
            generate_codes(node.left, prefix + "0", code_map)
        if node.right:
            generate_codes(node.right, prefix + "1", code_map)
    return code_map

# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    # Если freqs пустой или содержит 1 элемент, возвращаем None
    if not freqs or len(freqs) <= 1:
        return None
    
    # Если строка пустая, возвращаем пустую строку
    if not s:
        return ""
    
    root = build_tree(freqs)
    if root is None:
        return None
    
    code_map = generate_codes(root)
    
    result = ""
    for char in s:
        if char not in code_map:
            return None
        result += code_map[char]
    
    return result

# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    # Если freqs пустой или содержит 1 элемент, возвращаем None
    if not freqs or len(freqs) <= 1:
        return None
    
    # Если bits пустая строка, возвращаем пустую строку
    if not bits:
        return ""
    
    root = build_tree(freqs)
    if root is None:
        return None
    
    result = ""
    current = root
    
    for bit in bits:
        if bit == '0':
            current = current.left
        elif bit == '1':
            current = current.right
        else:
            return None
        
        if current is None:
            return None
        
        if current.is_leaf():
            result += current.char
            current = root
    
    return result

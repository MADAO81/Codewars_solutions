# https://www.codewars.com/kata/57680d0128ed87c94f000bfd/train/python

def find_word(board, word):
    if not board or not board[0] or not word:
        return False
    
    rows = len(board)
    cols = len(board[0])
    
    # Quick check: count characters in board vs word
    # This is an optimization to quickly reject impossible words
    from collections import Counter
    board_chars = Counter()
    for row in board:
        board_chars.update(row)
    word_chars = Counter(word)
    
    # If any character in word appears more times than in board, impossible
    for char, count in word_chars.items():
        if board_chars[char] < count:
            return False
    
    # Directions: 8 adjacent cells (horizontal, vertical, diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    def dfs(row, col, index, visited):
        # If we've matched all characters, success
        if index == len(word):
            return True
        
        # Check bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        
        # Check if cell is already visited or doesn't match current character
        if visited[row][col] or board[row][col] != word[index]:
            return False
        
        # Mark current cell as visited
        visited[row][col] = True
        
        # Try all 8 adjacent cells
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if dfs(new_row, new_col, index + 1, visited):
                return True
        
        # Backtrack: unmark current cell
        visited[row][col] = False
        return False
    
    # Try starting from each cell that matches the first character
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                visited = [[False] * cols for _ in range(rows)]
                if dfs(i, j, 0, visited):
                    return True
    
    return False

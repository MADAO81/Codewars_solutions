# https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python

# def street_fighter_selection(fighters, initial_position, moves):
#     position = list(initial_position)
#     result = []
#     for ch in moves:
#         if ch == "up":
#             position[0] -= 1
#         if ch == "down":
#             position[0] += 1
#         if ch == "right":
#             position[1] += 1
#         if ch == "left":
#             position[1] -= 1
#         if position[0] < 0:
#             position[0] = 0
#         if position[0] == len(fighters):
#             position[0] = len(fighters) - 1
#         result.append(fighters[position[0] % len(fighters)][position[1]%len(fighters[0])])
#     return result 



MOVES = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

def street_fighter_selection(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dy, dx = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters):
            y -= dy
        x = (x + dx) % len(fighters[y])
        hovered_fighters.append(fighters[y][x])
    return hovered_fighters

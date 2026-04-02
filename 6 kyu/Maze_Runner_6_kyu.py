# https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python


# def maze_runner(maze, directions):
#     current_pos, N = find_initial_position(maze), len(maze)
#     for direction in directions:
#         if direction in ("N", "S"):
#             current_pos[1] += -1 if direction == "N" else 1
#         else:
#             current_pos[0] += -1 if direction == "W" else 1
#         X,Y = current_pos[0], current_pos[1]
#         if X >= N or Y >= N or X <0 or Y < 0 or maze[Y][X] == 1:
#             return "Dead"
#         elif maze[Y][X] == 3:
#             return "Finish"
#     return "Lost"


# def find_initial_position(maze):
#     for y in range(len(maze)):
#         for x in range(len(maze[y])):
#             if maze[y][x] == 2:
#                 return [x,y]



def maze_runner(maze, directions):
    n = len(maze)
    
    # find start point
    for i in range(n):
        if 2 in maze[i]:
            row = i
            col = maze[row].index(2)
            break
    
    # follow directions
    for step in directions:
        if   step == "N": 
          row -= 1
        elif step == "S": 
          row += 1
        elif step == "E": 
          col += 1
        elif step == "W": 
          col -= 1
        
        # check the result
        if row < 0 or col < 0 or row == n or col == n or maze[row][col] == 1:
            return "Dead"
        elif maze[row][col] == 3:
            return "Finish"
    
    return "Lost"

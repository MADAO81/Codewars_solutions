# https://www.codewars.com/kata/549ee8b47111a81214000941/train/python

from collections import deque

def knight(p1, p2):
    a,b = (ord(p1[0])-97, int(p1[1])-1), (ord(p2[0])-97, int(p2[1])-1)
    q, v = deque([(*a, 0)]), {a}
    while q:
        x,y,d = q.popleft()
        for dx,dy in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
            nx,ny = x+dx, y+dy
            if (nx,ny) == b: return d+1
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx,ny) not in v:
                v.add((nx,ny)); q.append((nx,ny,d+1))
    return 0

import sys
from collections import deque 
import itertools

input = sys.stdin.readline

def BFS() :
    while tomato :
        x,y = tomato.popleft()
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        for i in range(4) :
            nx, ny = x + dx[i] , y + dy[i]
            
            if 0 <= nx < height and 0 <= ny < width and box[nx][ny] == 0 :
                box[nx][ny] = box[x][y] + 1
                tomato.append( [nx,ny] )
    

width, height = map(int, input().split())

box = [ list(map(int, input().split())) for _ in range(height) ]

tomato = deque([])
# 토마토가 있는 위치를 먼저 찾는다.
for i in range(height) :
    for j in range(width) :
        if box[i][j] == 1 :
            tomato.append( [i,j] )
            
            
BFS()

# 익지 않은 토마토가 있는지 ?
tomato = list(itertools.chain(*box))

print( tomato )
print( -1 if 0 in tomato else max(tomato)-1 )
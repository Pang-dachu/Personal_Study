import sys
from collections import deque
import itertools

input = sys.stdin.readline

def BFS() :
    dx,dy,dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]
    
    while tomato :
        z,y,x = tomato.popleft()
        for i in range(6) :
            nx,ny,nz = dx[i] + x, dy[i] + y, dz[i] + z
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][ny][nx] == 0 :
                box[nz][ny][nx] = box[z][y][x] + 1
                tomato.append( [nz,ny,nx] )     

M,N,H = map( int, input().split() )

tomato = deque([])
box = [ [ list(map(int, input().split())) for _ in range(N) ] for _ in range(H) ]

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if box[i][j][k] == 1 :
                tomato.append( [i,j,k] )


# BFS 실행 
BFS()

# 0이 있는지, 없다면 최대값 출력 
box = list(itertools.chain(*box))
box = list(itertools.chain(*box))

print( -1 if 0 in box else max(box)-1 )
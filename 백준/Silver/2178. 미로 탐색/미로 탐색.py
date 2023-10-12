import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy,sx):
    queue = deque()
    visited = [[0]*M for _ in range(N)]
    visited[sy][sx] = 1
    queue.append((sy,sx))
    while queue:
        cy, cx = queue.popleft()

        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and board[ny][nx] == 1:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((ny,nx))
    return visited[N-1][M-1]
    

if __name__=='__main__':
    N, M = map(int ,input().split())
    board = [list(map(int,input().strip())) for _ in range(N)]
    print(bfs(0,0))
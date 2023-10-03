import sys
from collections import deque
input = sys.stdin.readline


dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(sy, sx):
    stack = []
    stack.append((sy,sx))
    while stack:
        cy, cx = stack.pop()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=ny<N and 0<=nx<M:
                if board[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    stack.append((ny,nx))

def bfs(sy,sx):
    board[sy][sx] = 0
    queue = deque()
    queue.append((sy,sx))
    size = 1
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=ny<N and 0<=nx<M:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    queue.append((ny,nx))
                    size += 1
    return size


if __name__=='__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0
    max_size = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i, j)
                count += 1
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                max_size = max(max_size, bfs(y,x))
    print(count, max_size, sep='\n')

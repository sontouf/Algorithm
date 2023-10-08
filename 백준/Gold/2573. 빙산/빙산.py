import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy,sx):
    queue = deque()
    visited[sy][sx] = 1
    queue.append((sy,sx))
    while queue:
        cy,cx = queue.popleft()

        for i in range(4):
            ny,nx = dy[i] + cy, dx[i] + cx

            if 0<=ny<N and 0<=nx<M:
                if board[ny][nx] == 0:
                    visited[cy][cx] += 1

                if visited[ny][nx] == 0 and board[ny][nx] != 0:
                    queue.append((ny,nx))
                    visited[ny][nx] = 1



if __name__=='__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    year = 0
    while True:
        count = 0
        for i in range(N):
            for j in range(M):
                if visited[i][j] == 0 and board[i][j] != 0:
                    bfs(i,j)
                    count += 1
        for i in range(N):
            for j in range(M):
                if visited[i][j] != 0:
                    board[i][j] -= (visited[i][j]-1)
                    visited[i][j] = 0
                    if board[i][j] < 0:
                        board[i][j] = 0
        if count == 0:
            print(0)
            exit(0)
        if count >= 2:
            print(year)
            exit(0)
        year += 1
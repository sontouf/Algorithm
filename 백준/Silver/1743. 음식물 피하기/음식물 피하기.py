import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]
def bfs(sy,sx):
    count = 1
    queue = deque()
    queue.append((sy,sx))
    board[sy][sx] = 0
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=ny<N and 0<=nx<M:
                if board[ny][nx] == 1:
                    board[ny][nx] = 0
                    queue.append((ny,nx))
                    count += 1
    return count
    

if __name__=='__main__':
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        board[r-1][c-1] = 1
    max_size = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                max_size = max(max_size, bfs(i, j))
    print(max_size)
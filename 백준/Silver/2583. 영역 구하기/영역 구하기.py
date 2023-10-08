import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]


def dfs(sy,sx):
    board[sy][sx] = 1
    stack = []
    stack.append((sy,sx))
    size = 0
    while stack:
        cy,cx = stack.pop()
        size += 1
        for i in range(4):
            ny, nx = dy[i]+cy, dx[i]+cx

            if 0<=ny<M and 0<=nx<N:
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    stack.append((ny,nx))
    return size

if __name__=='__main__':
    M, N, K = map(int, input().split())
    board = [[0] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1,y2):
            for j in range(x1, x2):
                board[i][j] = 1
    count = 0
    size = []
    for i in range(M):
        for j in range(N):
            if board[i][j] == 0:
                size.append(dfs(i,j))
                count += 1
    print(count)
    size.sort()
    print(*size)
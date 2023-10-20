import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(sy, sx):
    stack = []
    board[sy][sx] = '.'
    stack.append((sy,sx))
    while stack:
        cy, cx = stack.pop()
        
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=ny<H and 0<=nx<W:
                if board[ny][nx] == '#':
                    board[ny][nx] = '.'
                    stack.append((ny,nx))

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        count = 0
        H, W = map(int, input().split())
        board = [list(input().strip()) for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if board[i][j] == '#':
                    dfs(i, j)
                    count += 1
        print(count)

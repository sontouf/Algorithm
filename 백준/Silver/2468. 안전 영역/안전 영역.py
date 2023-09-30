import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def painting(height):
    for y in range(N):
        for x in range(N):
            if height < graph[y][x]:
                paint[y][x] = 0
            else:
                paint[y][x] = 1

def dfs(sy, sx, paint):
    paint[sy][sx] = 1
    stack = []
    stack.append((sy,sx))
    while stack:
        cy, cx = stack.pop()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=ny<N and 0<=nx<N:
                if paint[ny][nx] == 0:
                    paint[ny][nx] = 1
                    stack.append((ny,nx))
        


if __name__=='__main__':
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    paint = [[0] * N for _ in range(N)]
    max_value = 0
    for i in range(N):
        if max_value < max(graph[i]):
            max_value = max(graph[i])
    max_size = 0
    count = 0
    for i in range(max_value):
        painting(i)
        for y in range(N):
            for x in range(N):
                if paint[y][x] == 0:
                    dfs(y, x, paint)
                    count += 1
        if max_size < count:
            max_size = count
        count = 0
    print(max_size)
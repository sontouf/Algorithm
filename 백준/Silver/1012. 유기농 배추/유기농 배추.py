import sys

input = sys.stdin.readline


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(sy, sx):
    stack = []
    stack.append((sy, sx))
    visited[sy][sx] = 1

    while stack:
        cy, cx = stack.pop()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    stack.append((ny, nx))
                    visited[ny][nx] = 1

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0] * M for _ in range(N)]
        visited = [[0] * M for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, input().split())    
            graph[Y][X] = 1
    
        count = 0
        for y in range(N):
            for x in range(M):
                if graph[y][x] == 1 and visited[y][x] == 0:
                    dfs(y, x)
                    count += 1
        print(count)

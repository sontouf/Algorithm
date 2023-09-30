import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(sy,sx):
    visited[sy][sx] = 1
    stack = []
    stack.append((sy,sx))
    color = graph[sy][sx]
    while stack:
        cy ,cx = stack.pop()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx

            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx] == 0 and graph[ny][nx] == color:
                    visited[ny][nx] = 1
                    stack.append((ny,nx))

if __name__=='__main__':
    N = int(input())
    graph = [list(input().strip()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
 
    count1 = 0
    count2 = 0
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                dfs(y,x)
                count1 += 1
    
    for y in range(N):
        for x in range(N):
            if graph[y][x] == 'G':
                graph[y][x] = 'R'
    visited = [[0] * N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                dfs(y,x,)
                count2 += 1
    print(count1, count2)
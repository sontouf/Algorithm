import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]


def dfs(sy ,sx):
    global answer
    visited[graph[sy][sx]] = 1
    path.append(graph[sy][sx])
    if answer < len(path):
        answer = len(path)
    
    for i in range(4):
        ny = dy[i] + sy
        nx = dx[i] + sx
        if 0<=ny<R and 0<=nx<C:
            if visited[graph[ny][nx]] == 0:
                dfs(ny, nx)
                visited[graph[ny][nx]] = 0
                path.pop()

if __name__ == '__main__':
    R, C = map(int, input().split())
    graph = [list(map(lambda x:ord(x)-ord('A'), input().strip())) for _ in range(R)]
    visited = [0] * 26
    path = []
    answer = 0
    dfs(0, 0)
    print(answer)

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,-1,1,1,-1,1,-1]

def dfs(ocean): # 바다
    island = set(); h = 0
    for y, x in ocean:
        if not visited[y][x]:
            island |= bfs(y,x,4,0)
    for y, x in island:
        if not visited[y][x]:
            h = max(h,dfs(bfs(y,x,8,1))+1)
    if len(result) == h:
        result.append(0)
    result[h] += 1
    return h


def bfs(sy,sx,d,n): # 바다탐색하면 섬, 섬을 탐색하면 바다의 좌표 더미 리턴
    queue = deque([(sy,sx)])
    S = set()
    while queue:
        cy, cx = queue.popleft()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = 1
        for i in range(d):
            ny, nx = dy[i]+cy,dx[i]+cx
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                if board[ny][nx] == n:
                    queue.append((ny,nx))
                else:
                    S.add((ny,nx))
    return S

if __name__=='__main__':
    N, M = map(int, input().split())
    M += 2
    board = [[0] * M] + [[0] + [*map(lambda x:1 if x=='x' else 0, input().strip())] + [0] for _ in range(N)] + [[0] * M]
    N += 2

    visited = [[0] * M for _ in range(N)]
    result = []
    dfs([(0,0)])
    result.pop() # 현재 시작자체를 하나의 섬 안이라고 볼수있기때문에
    print(*result if result else [-1])
import sys
from collections import deque
input = sys.stdin.readline

def bfs(r):
    queue = deque()
    visited[r] = 1
    count = 1
    queue.append(r)
    while queue:
        cur = queue.popleft()
        graph[cur].sort()
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                count += 1
                visited[nxt] = count
                queue.append(nxt)


if __name__=='__main__':
    N, M, R = map(int ,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        u, v = map(int ,input().split())
        graph[u].append(v)
        graph[v].append(u)
    bfs(R)
    for i in range(1, N+1):
        print(visited[i])

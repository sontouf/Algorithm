import sys
from collections import deque

input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for nxt in graph[v]:
        if visited[nxt] == 0:
            dfs(nxt)

def bfs(v):
    visited[v] = 1
    queue = deque([v])
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for nxt in graph[cur]:
                if visited[nxt] == 0:
                    visited[nxt] = 1
                    queue.append(nxt)

if __name__ == '__main__':
    N, M, V= map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        key1, key2 = map(int, input().split())
        graph[key1].append(key2)
        graph[key2].append(key1)

    for i in graph:
        i.sort()
   
    visited = [0] * (N+1)
    dfs(V)
    print()

    visited = [0] * (N+1)
    bfs(V)
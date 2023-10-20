import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, find):
    queue = deque()
    queue.append((start, 0))
    visited = [0] * (N + 1)
    visited[start] = 1
    while queue:
        v, d = queue.popleft()

        if v == find:
            return d
        for nv, l in graph[v]:
            if visited[nv] == 0:
                visited[nv] = 1
                queue.append((nv, d+l))

if __name__=='__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    distance = [0] * (N+1)
    for i in range(N-1):
        s, e, distance = map(int, input().split())
        graph[s].append((e, distance))
        graph[e].append((s, distance))
    for _ in range(M):
        n1, n2 = map(int, input().split())
        print(bfs(n1, n2))
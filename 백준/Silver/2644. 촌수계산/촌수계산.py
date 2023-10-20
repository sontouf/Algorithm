import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    visited[v] = 1
    distance[v] = 0
    queue.append(v)
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
                distance[nxt] = distance[cur] + 1

if __name__=='__main__':
    N = int(input())
    v1, v2 = map(int, input().split())
    T = int(input())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    distance = [-1] * (N+1)
    for _ in range(T):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    bfs(v1)
    print(distance[v2])

        

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    visited = [0] * (N+1)
    distance = [1] * (N+1)
    queue = deque()
    visited[v] = 1
    queue.append(v)
    while queue:
        cur =  queue.popleft()

        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
                distance[nxt] = distance[cur] + 1
    return sum(distance)


if __name__=='__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    result = N*N
    result_V = 0
    sum_distance = 0
    for _ in range(M):
        key1, key2 = map(int, input().split())
        graph[key1].append(key2)
        graph[key2].append(key1)
    for i in range(1, N+1):
        sum_distance = bfs(i)
        if result > sum_distance:
            result = sum_distance
            result_V = i
    print(result_V)

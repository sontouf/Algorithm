import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    visitead = [-1] * (N+1)
    visitead[v] = 0
    max_value = [0,0]
    queue.append(v)
    while queue:
        cur = queue.popleft()
        for nxt, d in graph[cur]:
            if visitead[nxt] == -1:
                visitead[nxt] = visitead[cur] + d
                queue.append(nxt)
                if max_value[0] < visitead[nxt]:
                    max_value = visitead[nxt], nxt
    return max_value


    


if __name__=='__main__':
    N = int(input())
    graph = [[] for _ in range(N+1)]
    max_distance = 0
    for _ in range(N):
        arr = list(map(int, input().split()))
        for i in range(1,len(arr)-2, 2):
                graph[arr[0]].append((arr[i], arr[i+1]))
    max_distance, i = bfs(1)
    max_distance, i = bfs(i)
    print(max_distance)
import sys
input = sys.stdin.readline

def dfs(start:int):
    visited[start] = 1
    for nxt in graph[start]:
        if visited[nxt] == 0:
            dfs(nxt)



if __name__=='__main__':
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        key, value = map(int, input().split())
        graph[key].append(value)
        graph[value].append(key)
    visited = [0] * (N+1)
    dfs(1)
    print(sum(visited)-1)

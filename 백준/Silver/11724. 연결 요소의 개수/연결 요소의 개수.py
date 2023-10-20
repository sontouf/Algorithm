import sys
input = sys.stdin.readline

def dfs(v):
    path = []
    visited[v] = 1
    path.append(v)
    while path:
        cur = path.pop()
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                path.append(nxt)
                


            
        

if __name__=='__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        key, value = map(int, input().split())
        graph[key].append(value)
        graph[value].append(key)
    
    visited = [0] * (N+1)
    count = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            count += 1
    print(count)
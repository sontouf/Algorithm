import sys
input = sys.stdin.readline


def dfs(cur):
    visited[cur] = 1
    stack = []
    stack.append(cur)
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                stack.append(nxt)
            else: # 니가 마지막이야.
                parent_node[cur] = nxt

    
    

if __name__=='__main__':
    N = int(input())
    parent_node = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(N-1):
        key1, key2 = map(int,input().split())
        graph[key1].append(key2)
        graph[key2].append(key1)
    dfs(1)

    for i in range(2, N+1):
        print(parent_node[i])
        


import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(cur:int)->int:
    visited[cur] = 1
    nxt = graph[cur]
    cycle.append(cur)

    if visited[nxt] == 0:
        return dfs(nxt)
    else:
        if nxt in cycle:
            return cycle.index(cur) - cycle.index(nxt) + 1
        return 0


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        count = 0
        graph = [0] + list(map(int, input().split()))
        visited = [0] * (N + 1)
        for i in range(1,N+1):
            if visited[i] == 0:
                cycle = []
                count += dfs(i)
        print(N-count)

import sys
input = sys.stdin.readline

def dfs(path):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(1, N+1):
        if len(path) != 0 and i >= max(path):
            dfs([*path, i])
        elif len(path) == 0:
            dfs([*path, i])


if __name__ == '__main__':
    N, M = map(int, input().split())

    dfs([])
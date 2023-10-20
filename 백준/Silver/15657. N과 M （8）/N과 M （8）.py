import sys
input = sys.stdin.readline

def dfs(path):
    if len(path) == M:
        print(*path)
        return
    
    for i in nums:
        if path and i >= max(path):
            dfs([*path, i])
        elif not path:
            dfs([*path, i])



if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    dfs([])
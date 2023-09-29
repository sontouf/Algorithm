import sys
input = sys.stdin.readline

def dfs():
    if len(path) == M:
        print(*path)
        return
    
    non_path = -1
    for i in range(N):
        if visited[i] == 0 and non_path != nums[i]:
            if not path or path and nums[i] >= max(path):
                visited[i] = 1
                path.append(nums[i])
                non_path = nums[i]
                dfs()
                path.pop()
                visited[i] = 0



if __name__=='__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    visited = [0] * N
    path = []
    dfs()
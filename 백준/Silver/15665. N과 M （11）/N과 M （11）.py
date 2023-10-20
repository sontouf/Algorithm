import sys
input = sys.stdin.readline

def dfs():
    if len(path) == M:
        print(*path)
        return
    
    non_path = -1
    for i in range(N):
        if non_path != nums[i]:
            path.append(nums[i])
            non_path = nums[i]
            dfs()
            path.pop()



if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    path = []
    dfs()
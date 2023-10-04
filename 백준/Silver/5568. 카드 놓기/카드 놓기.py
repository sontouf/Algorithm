import sys
input = sys.stdin.readline


def dfs(arr):
    if len(picked) == K:
        result.add(arr)
        return
    for i in range(len(nums)):
        if i not in picked:
            picked.append(i)
            dfs(arr+nums[i])
            picked.pop()        




if __name__=='__main__':
    N = int(input())
    K = int(input())
    nums = [input().strip() for _ in range(N)]
    result = set()
    picked = []
    dfs("")
    print(len(result))
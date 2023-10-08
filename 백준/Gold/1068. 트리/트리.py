import sys
input = sys.stdin.readline

def dfs(removeNode, parentList):
    parentList[removeNode] = -2
    for i in range(N):
        if removeNode == parentList[i]:
            dfs(i, parentList)

if __name__=='__main__':
    N = int(input())
    parentList = list(map(int, input().split()))
    removeNode = int(input())
    dfs(removeNode, parentList)
    count = 0
    for i in range(N):
        if parentList[i] != -2 and i not in parentList:
            count += 1
    print(count)

import sys
input = sys.stdin.readline

def dfs(i, m,snowsize,flag): # i 위치에서의 눈덩이 크기.
    if m == 0 or i >= N+1:
        return snowsize
    snowsize = snowsize // flag + arr[i]
    return max(dfs(i+1, m-1, snowsize,1), dfs(i+2,m-1,snowsize,2))
    

if __name__=='__main__':
    N, M = map(int, input().split())
    arr = [0]+list(map(int, input().split()))
    print(dfs(0,M+1,1,1))
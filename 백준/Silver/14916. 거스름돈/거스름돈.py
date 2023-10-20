import sys
input = sys.stdin.readline

if __name__=='__main__':
    N = int(input())
    dp = [-1,-1,1,-1,2,1,3,2,4,3]
    if N >= 10:
        for i in range(10, N+1):
            dp.append(dp[i-5] + 1)
    print(dp[N])
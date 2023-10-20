import sys
input = sys.stdin.readline

def f(k, n):
    if k == 0:
        dp[k][n] = n
        return dp[k][n]
    if dp[k][n] != 0:
        return dp[k][n]
    for i in range(1, n+1):
        dp[k][n] += f(k-1,i)
    return dp[k][n]
if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        dp = [[0] * (n+1) for _ in range(k+1)]
        print(f(k, n))
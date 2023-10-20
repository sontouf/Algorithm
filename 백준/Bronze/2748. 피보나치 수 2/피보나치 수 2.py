import sys
input = sys.stdin.readline

def f(N):
    if N == 0 or N == 1:
        return N
    if dp[N] != -1:
        return dp[N]
    dp[N] = f(N-1) + f(N-2)
    return dp[N]


if __name__=='__main__':
    N = int(input())
    dp = [-1] * (N+1)
    print(f(N))
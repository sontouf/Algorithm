import sys
input = sys.stdin.readline

def f(v):
    if v == 0 or v == 1:
        return 1
    if dp[v] != 0:
        return dp[v]
    result = 0
    if v % 2 == 0:
        for i in range(v//2):
            result += 2 * f(i) * f(v-1-i)
    else:
        for i in range((v-1) // 2):
            result += 2 * f(i) * f(v-1-i)
        result += f((v-1)//2)**2
    dp[v] = result
    return result


if __name__=='__main__':
    N = int(input())
    dp = [0] * (N+1)
    print(f(N))
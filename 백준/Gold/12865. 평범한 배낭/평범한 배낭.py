def f(idx, total):
    if idx == N or total == K:
        return 0
    
    if dp[idx][total] !=-1:
        return dp[idx][total]
    
    w, v = arr[idx]
    result = f(idx + 1, total)
    if total + w <= K:
        result = max(result, f(idx + 1, total + w) + v)
    dp[idx][total] = result
    return result

if __name__=='__main__':
    N, K = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * K for _ in range(N)]
    print(f(0, 0))
import sys
input = sys.stdin.readline

def dfs(n, m):
    if n == 1 or m == 1: return 1
    result = 1
    base = n
    index = dfs(n, phi(m)) + phi(m)
    while index:
        if index & 1:
            result = (result * base) % m
        index >>= 1
        base = (base**2) % m

    return result

        

def phi(n):
    result = n
    p = 2
    while p*p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= (result // p)
        p += 1

    if n > 1:
        result -= (result // n)
    return result


if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(dfs(N,M) % M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
for _ in range(M):
    first, second = map(int, input().split())
    temp = basket[first-1:second]
    temp.reverse()
    basket[first-1:second] = temp
print(*basket)
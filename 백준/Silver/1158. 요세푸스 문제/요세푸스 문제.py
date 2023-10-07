import sys
from collections import deque
input = sys.stdin.readline

if __name__=='__main__':
    N, K = map(int, input().split())
    arr = deque()
    for i in range(1, N+1):
        arr.append(i)
    picked = [0] * (N+1)
    order = []
    start = 1
    while True:
        if len(order) == N:
            break
        if len(order) == N - 1:
            order.append(arr.pop())
            break
        for _ in range(K):
            cur = arr.popleft()
            arr.append(cur)
        order.append(arr.pop())
    print("<", end='')
    for i in range(N-1):
        print(order[i],', ', sep='', end='')
    print(order[N-1],end='')
    print(">",end='')
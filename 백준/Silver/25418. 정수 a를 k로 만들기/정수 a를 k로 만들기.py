import sys
from collections import deque
input = sys.stdin.readline

if __name__=='__main__':
    A, K = map(int, input().split())
    count = 0
    while True:
        if K == A:
            break
        if K % 2 == 0 and K >= 2 * A:
            K >>= 1
        else:
            K -= 1
        count += 1
    print(count)
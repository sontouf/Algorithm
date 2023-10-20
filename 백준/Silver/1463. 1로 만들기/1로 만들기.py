import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        cur = queue.popleft()
        if cur == 1:
            print(distance[cur])
            break
        if cur % 3 == 0 and not distance[cur // 3]:
                distance[cur // 3] = distance[cur] + 1
                queue.append(cur // 3)
        if cur % 2 == 0 and not distance[cur // 2]:
                distance[cur // 2] = distance[cur] + 1
                queue.append(cur // 2)
        if not distance[cur - 1]:
            distance[cur - 1] = distance[cur] + 1
            queue.append(cur - 1)
    

if __name__=='__main__':
    N = int(input())
    distance = [0] *(N+1)
    bfs(N)

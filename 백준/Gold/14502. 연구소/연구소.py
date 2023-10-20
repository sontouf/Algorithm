import sys
import copy
from collections import deque


input = sys.stdin.readline


dy = [-1,1,0,0]
dx = [0,0,-1,1]


def bfs(sy, sx):
    queue = deque()
    queue.append((sy,sx))
    while queue:
        cy,cx = queue.popleft()
        for i in range(4):
            ny = dy[i] + cy
            nx = dx[i] + cx
            
            if 0<=ny<N and 0<=nx<M:
                if copy_graph[ny][nx] == 0:
                    copy_graph[ny][nx] = 2
                    queue.append((ny,nx))





if __name__=='__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    zero = []
    max_count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                zero.append((y, x))

    zero_l = len(zero)
    for i in range(zero_l-2):
        for j in range(i+1, zero_l-1):
            for k in range(j+1, zero_l):
                copy_graph = copy.deepcopy(graph)
                count = 0
                cy1, cx1 = zero[i]
                cy2, cx2 = zero[j]
                cy3, cx3 = zero[k]
                copy_graph[cy1][cx1] = 1
                copy_graph[cy2][cx2] = 1
                copy_graph[cy3][cx3] = 1
                for y in range(N):
                    for x in range(M):
                        if copy_graph[y][x] == 2:
                            bfs(y, x) # 바이러스
                for y in range(N):
                    for x in range(M):
                        if copy_graph[y][x] == 0:
                            count += 1
                max_count = max(max_count,count)
    print(max_count)

                    
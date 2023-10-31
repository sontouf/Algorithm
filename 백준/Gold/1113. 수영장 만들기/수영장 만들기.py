import sys
from collections import deque
input = sys.stdin.readline


dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx, height):
	queue = deque()
	queue.append((sy,sx))
	visited[sy][sx] = 1
	count = 1
	flag = 1
	while queue:
		cy, cx = queue.popleft()
		for i in range(4):
			ny, nx = dy[i] + cy, dx[i] + cx

			if 0<=ny<N and 0<=nx<M:
				if visited[ny][nx] == 0 and waterpool[ny][nx] <= height:
					visited[ny][nx] = 1
					count += 1
					queue.append((ny, nx))
			else :
				flag = 0
	if flag:
		return count
	return 0

	

if __name__=='__main__':
	N, M = map(int, input().split())
	waterpool = [list(map(int, list(input().strip()))) for _ in range(N)]
	result = 0
	for h in range(1, 9):
		visited = [[0] * M for _ in range(N)]
		for i in range(N):
			for j in range(M):
				if visited[i][j] == 0 and waterpool[i][j] <= h:
					result += bfs(i, j, h)
	print(result)


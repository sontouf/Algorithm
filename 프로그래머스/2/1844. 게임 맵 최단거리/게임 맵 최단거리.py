from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx, maps):
	N, M = len(maps), len(maps[0])
	queue = deque()
	queue.append((sy,sx))
	maps[sy][sx] = 2
	while queue:
		cy, cx = queue.popleft()

		for i in range(4):
			ny, nx = dy[i] + cy, dx[i] + cx

			if 0<=ny<N and 0<=nx<M:
				if maps[ny][nx] == 1:
					maps[ny][nx] = maps[cy][cx] + 1
					queue.append((ny, nx))
	return maps[N-1][M-1] - 1


def solution(maps):
	answer = bfs(0,0, maps)
	if answer <= 0:
		return -1
	return answer
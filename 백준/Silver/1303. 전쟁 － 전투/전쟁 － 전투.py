import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx, team):
	visited[sy][sx] = 1
	count = 1
	queue = deque()
	queue.append((sy,sx))
	while queue:
		cy ,cx = queue.popleft()
		for i in range(4):
			
			ny, nx = dy[i] + cy, dx[i] + cx
			if 0 <= ny < N and 0 <= nx < M:
				if board[ny][nx] == team and visited[ny][nx] == 0:
					visited[ny][nx] = 1
					queue.append((ny, nx))
					count += 1
	return count

def power(team):
	result = 0
	for i in range(N):
		for j in range(M):
			if board[i][j] == team and visited[i][j] == 0:
				temp = bfs(i, j, team)
				result += temp * temp
	return result

if __name__=='__main__':
	M, N = map(int , input().split())
	board = [list(map(lambda x : 0 if x == 'W' else 1, input().strip())) for _ in range(N)]
	visited = [[0] * M for _ in range(N)]
	power_w = power(0)
	visited = [[0] * M for _ in range(N)]
	power_b = power(1)
	print(power_w, power_b)


                
     
                

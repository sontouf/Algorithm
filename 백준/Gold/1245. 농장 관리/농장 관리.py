import sys
input = sys.stdin.readline

dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,-1,1,1,-1,-1,1]

def dfs(sy, sx):
	visited[sy][sx] = 1
	result = 1

	stack = []
	stack.append((sy, sx))
	while stack:
		cy, cx = stack.pop()

		for i in range(8):
			ny, nx = dy[i] + cy, dx[i] + cx
			if 0 <= ny < N and 0 <= nx < M:
				if board[ny][nx] > board[cy][cx]:
					result = 0
				if visited[ny][nx] == 0 and board[ny][nx] == board[cy][cx]:
					visited[ny][nx] = 1
					stack.append((ny, nx))
	return result
	

if __name__=='__main__':
	N, M = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(N)]
	visited = [[0] * M for _ in range(N)]
	mountain_peak = 0
	count = 0
	for i in range(N):
		for j in range(M):
			if board[i][j] > 0 and visited[i][j] == 0:
				mountain_peak = dfs(i,j)
				if mountain_peak == 1:
					count += 1
	print(count)
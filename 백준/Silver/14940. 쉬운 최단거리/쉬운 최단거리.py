import sys
from collections import deque
input = sys.stdin.readline


dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs():
	while queue:
		cy, cx = queue.popleft()
		for i in range(4):
			ny, nx = dy[i] + cy, dx[i] + cx
			if 0 <= ny < n and 0 <= nx < m:
				if board[ny][nx] == 1 and result_board[ny][nx] == -1:
					result_board[ny][nx] = result_board[cy][cx] + 1
					queue.append((ny, nx))


if __name__=='__main__':
	n, m = map(int, input().split())
	board = []
	queue = deque()
	result_board = [[-1] * m for _ in range(n)]
	for i in range(n):
		row = list(map(int, input().split()))
		for j in range(m):
			if row[j] == 2:
				queue.append((i, j))
				result_board[i][j] = 0
			elif row[j] == 0:
				result_board[i][j] = 0
		board.append(row)
	bfs()
	for i in range(n):
		print(*result_board[i], sep=' ')
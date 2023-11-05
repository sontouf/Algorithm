import sys
input = sys.stdin.readline


if __name__=='__main__':
	N, M = map(int, input().split())
	board = [list(map(int, input().strip())) for _ in range(N)]
	if N == 1 or  M == 1:
		print(1)
		exit(0)
	size = min(N, M)
	for k in range(size, 0, -1):
		find = 0
		for i in range(N-k+1):
			for j in range(M-k+1):
				if board[i][j] == board[i][j+k-1] == board[i+k-1][j] == board[i+k-1][j+k-1]:
					find = 1
		if find == 1:
			print(k*k)
			break


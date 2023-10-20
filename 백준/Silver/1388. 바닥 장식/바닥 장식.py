import sys
input = sys.stdin.readline

def checkrow(i):
	count  = 0
	j = 0
	while j < M:
		if board[i][j] == 0:
			count += 1
			while j < M:
				if board[i][j] != 0:
					break
				j += 1
		else:
			while j < M:
				if board[i][j] == 0:
					break
				j += 1
	return count


def checkcolumn(j):
	count  = 0
	i = 0
	while i < N:
		if board[i][j] == 1:
			count += 1
			while i < N:
				if board[i][j] != 1:
					break
				i += 1
		else:
			while i < N:
				if board[i][j] == 1:
					break
				i += 1
	return count

if __name__=='__main__':
	N, M = map(int, input().split())
	board = [list(map(lambda x: 0 if x == '-' else 1, input().strip())) for _ in range(N)]
	result = 0
	for i in range(N):
		result += checkrow(i)
	for i in range(M):
		result += checkcolumn(i)
	print(result)
	
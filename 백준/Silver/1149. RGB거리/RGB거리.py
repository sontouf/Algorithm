import sys
input = sys.stdin.readline

if __name__=='__main__':
	N = int(input())
	color = [list(map(int, input().split())) for _ in range(N)]
	
	for i in range(1, N):
		for j in range(3):
			color[i][j] = min(color[i-1][(j+1)%3], color[i-1][(j+2)%3]) + color[i][j]
	print(min(color[N-1][0], color[N-1][1], color[N-1][2]))

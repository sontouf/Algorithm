import sys
input = sys.stdin.readline

def dfs(v):
	for i in range(N):
		if graph[v][i] == 1 and visited[i] == 0:
			visited[i] = 1
			dfs(i)
			



if __name__=='__main__':
	N = int(input())
	graph = [list(map(int, input().split())) for _ in range(N)]
	for i in range(N):
		visited = [0 for _ in range(N)]
		dfs(i)
		print(*visited,sep=' ')
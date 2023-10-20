import sys
input = sys.stdin.readline

def dfs(v, arr):
	if len(arr) == K:
		print(*arr, sep='\n')
		exit(0)
	for nxt in range(v+1,N+1):
		if visited[nxt] == 0:
			for p in arr:
				if p not in graph[nxt]:
					break
			else:
				visited[nxt] = 1
				dfs(nxt,arr+[nxt])


if __name__=='__main__':
	K, N, F = map(int, input().split())
	if K > N:
		print(-1)
		exit(0)
	graph = [[] for _ in range(N + 1)]
	for _ in range(F):
		s, e = map(int ,input().split())
		graph[s].append(e)
		graph[e].append(s)
	
	for i in range(1, N+1):
		visited = [0] * (N + 1)
		visited[i] = 1
		dfs(i,[i])
	print(-1)
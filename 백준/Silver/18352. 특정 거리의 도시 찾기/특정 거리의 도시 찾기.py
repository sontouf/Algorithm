import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
	queue = deque()
	queue.append(v)
	visited = [0] * (N + 1)
	visited[v] = 1
	while queue:
		cur = queue.popleft()
		for nxt in graph[cur]:
			if visited[nxt] == 0:
				visited[nxt] = 1
				distance[nxt] = distance[cur] + 1
				queue.append(nxt)

if __name__=='__main__':
	N, M, K, X = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
	result = []
	distance = [0] * (N + 1)
	dfs(X)
	for i in range(1, N + 1):
		if distance[i] == K:
			result.append(i)

	if result:
		for i in result:
			print(i)
	else:
		print(-1)

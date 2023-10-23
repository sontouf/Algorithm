import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
	queue = deque([s])
	visited[s] = 1
	order = 1
	while queue:
		cur = queue.popleft()
		visited[cur] = order
		order += 1
		for nxt in graph[cur]:
			if visited[nxt] == 0:
				visited[nxt] = 1
				queue.append(nxt)


if __name__=='__main__':
	N, M, R = map(int, input().split())
	graph = [[] for _ in range(N + 1)]
	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	for i in range(1, N + 1):
		graph[i].sort(reverse=True)
	visited = [0] * (N + 1)
	bfs(R)
	print(*visited[1:], sep='\n')
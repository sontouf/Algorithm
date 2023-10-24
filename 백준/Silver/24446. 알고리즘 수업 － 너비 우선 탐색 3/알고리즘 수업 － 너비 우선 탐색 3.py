import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
	visited = [0] * (N + 1)
	visited[s] = 1
	queue = deque()
	queue.append(s)
	distance[s] = 0
	while queue:
		cur = queue.popleft()

		for nxt in graph[cur]:
			if visited[nxt] == 0:
				visited[nxt] = 1
				queue.append(nxt)
				distance[nxt] = distance[cur] + 1	

if __name__=='__main__':
	N, M, R = map(int, input().split())
	graph = [[] for _ in range(N + 1)]
	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	distance = [-1] * (N + 1)
	bfs(R)
	print(*distance[1:], sep='\n')
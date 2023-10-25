import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
	queue = deque()
	queue.append(s)
	visited[s] = 0
	distance[s] = 0
	num = 1
	while queue:
		cur = queue.popleft()
		visited[cur] = num
		num += 1
		for nxt in graph[cur]:
			if visited[nxt] == -1:
				visited[nxt] = 0
				queue.append(nxt)
				distance[nxt] = distance[cur] + 1


if __name__=='__main__':
	N, M, R = map(int, input().split())
	graph = [[] for _ in range(N + 1)]
	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	visited = [-1] * (N + 1)
	distance = [0] * (N + 1)
	for i in range(1, N + 1):
		graph[i].sort()
	bfs(R)
	total = 0
	for i in range(1, N + 1):
		total += visited[i] * distance[i]
	print(total)

import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
	visited = [0] * (N + 1)
	visited[start] = 1
	queue = deque()
	queue.append(start)
	distance = [0] * (N + 1)
	max_distance = 0
	max_node = start
	while queue:
		cur = queue.popleft()

		for nxt, n_d in graph[cur]:
			if visited[nxt] == 0:
				visited[nxt] = 1
				distance[nxt] = distance[cur] + n_d
				if max_distance < distance[nxt]:
					max_distance = distance[nxt]
					max_node = nxt
				queue.append(nxt)
	return (max_distance, max_node)

if __name__=='__main__':
	N = int(input())
	graph = [[] for _ in range(N + 1)]
	for _ in range(N-1):
		s, e, d = map(int, input().split())
		graph[s].append((e, d))
		graph[e].append((s, d))
	distance, node = bfs(1)
	distance, node = bfs(node)
	print(distance)

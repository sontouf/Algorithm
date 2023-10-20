import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
	queue = deque()
	queue.append(v)
	visited[v] = 0
	max_d = 0
	while queue:
		cur = queue.pop()

		for nxt, c in graph[cur]:
			if visited[nxt] == -1:
				visited[nxt] = visited[cur] + c
				queue.append(nxt)
				if max_d < visited[nxt]:
					max_d = visited[nxt]
	return max_d


if __name__=='__main__':
	N = int(input())
	graph = [[] for _ in range(N+1)]
	visited = [-1] * (N+1)
	for _ in range(N-1):
		a, b, c = map(int, input().split())
		graph[a].append((b, c))
		graph[b].append((a, c))
	print(bfs(1))
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
	queue = deque()
	queue.append(start)
	visited = [0] * (N + 1)
	visited[start] = 1
	distance = 0
	while queue:
		cur = queue.popleft()

		for nxt in graph[cur]:
			if visited[nxt] == 0:
				visited[nxt] = 1
				distance += 1
				queue.append(nxt)
	return distance
	

if __name__=='__main__':
	N, M = map(int, input().split())
	result = []
	max_cnt = 0
	graph = [[] for _ in range(N + 1)]
	for _ in range(M):
		e, s = map(int, input().split())
		graph[s].append(e)
	for i in range(1, N+1):
		cnt = bfs(i)
		if cnt > max_cnt:
			max_cnt = cnt
			result = []
			result.append(i)
		elif cnt == max_cnt:
			result.append(i)
	print(*result)

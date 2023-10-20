import sys
input = sys.stdin.readline

def dfs(v):
	stack = []
	visited = [0] * (N + 1)
	stack.append(v)
	order = [0] * (N + 1)
	cnt = 1
	while stack:
		cur = stack.pop()
		if visited[cur] == 1:
			continue
		visited[cur] = 1
		order[cur] = cnt
		cnt += 1
		for nxt in graph[cur]:
			if visited[nxt] == 0:
				stack.append(nxt)
	return order

if __name__=='__main__':
	N, M, R = map(int, input().split())
	graph = [[] for _ in range(N + 1)]
	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	for i in range(1, N+1):
		graph[i].sort()
	result = dfs(R)
	print(*result[1:], sep='\n')
import sys
input = sys.stdin.readline

def dfs(s):
	stack = []
	stack.append((s, 0))
	while stack:
		cur, depth = stack.pop()
		if visited[cur] != -1: continue
		visited[cur] = depth
		for nxt in graph[cur]:
			if visited[nxt] == -1:
				stack.append((nxt, depth + 1))


if __name__=='__main__':
	N, M, R = map(int, input().split())
	graph = [[] for _ in range(N + 1)]
	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	for i in range(1, N + 1):
		graph[i].sort()
	visited = [-1] * (N + 1)
	dfs(R)
	print(*visited[1:], sep='\n')
import sys
input = sys.stdin.readline

def dfs(s):
	stack = []
	stack.append((s, 0))
	while stack:
		cur, depth = stack.pop()
		if visited[cur] != -1:
			continue
		visited[cur] = depth
		for nxt in graph[cur]:
			if visited[nxt] == -1:
				stack.append((nxt, depth + 1))

if __name__=='__main__':
	n, k = map(int, input().split())
	graph = [[] for _ in range(n)]
	for _ in range(n-1):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	value = list(map(int, input().split()))
	visited = [-1] * n
	dfs(0)
	for i in range(n):
		if value[i] == k:
			print(visited[i])
			exit(0)
		
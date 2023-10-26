import sys
input = sys.stdin.readline


def dfs(s):
	stack = []
	num = 1
	stack.append((s, 0))
	while stack:
		cur, c_depth= stack.pop()
		if visited[cur] != 0:
			continue
		visited[cur] = num
		depth[cur] = c_depth
		num += 1
		for nxt in graph[cur]:
			if visited[nxt] == 0:
				stack.append((nxt, c_depth + 1))

if __name__=='__main__':
	N, M, R = map(int, input().split())
	graph = [[] for _ in range(N + 1)]

	for _ in range(M):
		s, e = map(int, input().split())
		graph[s].append(e)
		graph[e].append(s)
	visited = [0] * (N + 1)
	depth = [-1] * (N + 1)		
	for i in range(1, N + 1):
		graph[i].sort(reverse=True)
	dfs(R)
	total = 0
	for i in range(1, N + 1):
		total += visited[i] * depth[i]
	print(total)
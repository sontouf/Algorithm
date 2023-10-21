import sys
input = sys.stdin.readline


def dfs(s):
	stack = []
	stack.append(s)
	visited[s] = 1
	while stack:
		cur = stack.pop()
		for nxt in graph[cur]:
			if visited[nxt] != 100:
				visited[nxt] += 1
				stack.append(nxt)

if __name__=='__main__':
	N = int(input())
	graph = [[] for _ in range(N + 1)]
	for i in range(1, N):
		M = int(input())
		for m in list(map(int, input().split())):
			graph[i].append(m)
	visited = [0] * (N + 1)
	dfs(1)

	for i in range(1, N):
		if visited[i] == 100:
			print("CYCLE")
			exit(0)
	print("NO CYCLE")
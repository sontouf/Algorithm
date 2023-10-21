import sys
from collections import deque
input = sys.stdin.readline

def dfs(s, s_d, max_distance):
	dp = [max_distance] * (N + 1)
	queue = deque()
	queue.append((s, s_d))
	dp[s] = s_d
	while queue:
		cur, d = queue.popleft()
		if dp[cur] < d:
			continue
		for nxt, l in graph[cur]:
			n_d = l + d
			if n_d < dp[nxt]:
				dp[nxt] = n_d
				queue.append((nxt, n_d))
	return dp[N]


if __name__=='__main__':
	N, M = map(int, input().split())
	graph = [[] for _ in range(N + 1)]
	for _ in range(M):
		s, e, d = map(int, input().split())
		graph[s].append((e, d))
		graph[e].append((s, d))
	print(dfs(1, 0, 1000 * 50000))
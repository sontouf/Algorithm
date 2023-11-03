def dfs(n, start, computers, visited):
    for i in range(n):
         if computers[start][i] == 1:
            nxt = i
            if visited[nxt] == 0:
                visited[nxt] = 1
                dfs(n, nxt, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n, i, computers, visited)
            answer += 1
    return answer
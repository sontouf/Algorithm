# 1260 dfs와 bfs

```
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
```



dfs와 bfs은 그래프를 탐색할 때 방식의 차이가 있다.

dfs는 깊이 우선이기 때문에 인접 정점를 타고 들어가 끝까지 가고 말단 정점까지 가면 되돌아와 다른 갈림길로 가는 방법,

bfs는 너비 우선이기 때문에 인접 정점들을 다 확인하고 그 다음 높이의 정점으로 가는 특징이 있다. 인접 정점을 순서대로 확인해야 하므로 queue의 활용한다. 그래서 bfs는 정점 사이의 거리를 구하는 알고리즘에서 자주 사용된다.



또한 재귀와 스택은 메모리적 관점에서 동일하게 작동하므로 재귀로 구현했으면 스택도 동일하게 구현할 수 있는데 결과가 조금 다를 수 있다. 재귀는 인접 정점을  왼쪽부터(먼저 들어온 순서) 확인하지만 스택은 pop 연산으로 오른쪽부터(나중에 들어온 순서) 방문하는 특징이 있다.



__전체코드__

```python
import sys
from collections import deque
input = sys.stdin.readline


def dfs_recursion(v):
    visited[v] = 1
    print(v, end=' ')
    for nxt in graph[v]:
        if visited[nxt] == 0:
            dfs_recursion(nxt)

def dfs_stack(v):
    stack = []
    visited[v] = 1
    stack.append(v)
    while stack:
        cur = stack.pop()
        print(cur, end=' ')
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                stack.append(nxt)
def bfs(v):
    queue = deque()
    visited[v] = 1
    queue.append(v)
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)

if __name__=='__main__':
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    for i in range(N+1):
        graph[i].sort()
    visited = [0] * (N+1)
    dfs_recursion(V)
    print()
    visited = [0] * (N+1)
    dfs_stack(V)
    print()
    visited = [0] * (N+1)
    bfs(V)
    
        
```



1. 일단 입력이 들어온 대로 그래프를 만들어 준다. 이때 그래프는 양방향으로 만들어주어야 한다. 문제에서 요구한 대로 정점번호가 작은 것부터 방문해야 하므로 정렬도 해주자.

```python
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
        
    for i in range(N+1):
        graph[i].sort()
    # for i in graph:
    #   i.sort()
```

2. dfs는 재귀 버전과 스택버전 둘다 만들어보자. 제출할 때는 재귀버전만 쓰면된다. 스택버전은 나중에 들어온 순서를 먼저 방문하므로 재귀를 써야한다.

> dfs(v) : 정점 v 를 경로에 넣고 인접정점(nxt)을 확인하고 안 갔으면 정점 nxt 를 경로에 넣는다(dfs(nxt)).

```python
def dfs_recursion(v):
    visited[v] = 1 # 현재 정점에 방문했다.
    print(v, end=' ')
    for nxt in graph[v]: # 인접 정점을 확인하고
        if visited[nxt] == 0: # 안 갔으면 nxt에 방문하면 된다.
            dfs_recursion(nxt)
```

> 스택은 재귀 호출로 인한 스택 오버플로우를 방지할 수 있다. 스택에 다음에 갈 정점들을 쌓음으로 구현된다.

```python
def dfs_stack(v):
    stack = []
    visited[v] = 1
    stack.append(v)
    while stack:
        cur = stack.pop()
        print(cur, end=' ')
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                stack.append(nxt)
```



3. bfs는 dfs_stack에서 stack을 queue로만 바꾸면 된다.

```python
def bfs(v):
    queue = deque()
    visited[v] = 1
    queue.append(v)
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
```




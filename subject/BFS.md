# BFS

- 너비 우선 탐색(BFS; breadth-First-Search) : 시작 정점에서 가장 가까운 정점들은 모두 방문한다.
- 주로 `큐`를 사용하여 구현한다.



## BFS의 원리

1. 높이가 `1`인 노드들을 방문한다.
2. 높이가 `2`인 노드들을 방문한다.
3. ... 높이가 `k`인 노드들을 방문한다.



![graph](https://camo.githubusercontent.com/cf9ec9eafe052e3d3163c1d5cbf7239838da24f19160b4bc4352c561d6ef8453/68747470733a2f2f696d67312e6461756d63646e2e6e65742f7468756d622f523132383078302f3f73636f64653d6d746973746f72793226666e616d653d6874747073253341253246253246626c6f672e6b616b616f63646e2e6e6574253246646e25324662467a4844762532466274726743464778636f632532466b43534649534356626c4862764b6631657353525a4b253246696d672e6a7067)

BFS 로는 `0->1->2->3->4->5->6` 순으로 탐색할 것이다.



`BFS`의 구현

BFS는 `큐`를 사용하여 `반복`으로 구현할 수 있다.

## 재귀로는 구현할 수 없다.

BFS는 DFS와 달리 `재귀`로 구현할 수 없다. 큰 단위의 문제를 작은 단위의 문제로 생각하여 푸는 `재귀`의 특성을 생각해보면, BFS 의 방식에는 적용될 수 없음을 알 수 있다.



## 큐로 구현하기

```python
from collections import deque

graph = {
    0: [1,2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1, 6],
    4: [1],
    5: [2],
    6: [3]
}

visited = [0] * 7

def bfs(v): # root를 v라고 한다면
    queue = deque([v])
    visited[v] = 1 # 높이가 0인 노드 탐색
    
    while queue: # 높이가 k인 노드탐색
        cur = queue.popleft() 
        
        for nxt in graph[cur]: # 인접노드 찾아서 안갔으면 queue에 등록
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
                
bfs(0)
    
```

## BFS의 시간 복잡도

- 정점의 개수 `V`, 간선의 개수 `E`
  - `인접 리스트`로 그래프를 구현한 경우 : `O(V+E)`
    - 한 번 방문한 정점은 다시 방문하지 않는다.
    - 하나의 정점에서 다른 정점을 방문하는 횟수가 해당 정점의 차수가 같기 때문이다.



## 비연결 그래프에서 BFS

비연결 그래프에서 DFS와 같다



## 노드의 레벨 구하기

어떤 노드`v`의 레벨이 `k (k >= 0)`라면, 루트 노드부터 `v`까지 간선의 개수는 `k`이다. 어떻게 특정 노드의 레벨을 구할 수 있을까?



## BFS와 레벨

BFS를 레벨의 관점에서 보자. 레벨 `0`에 있는 모든 노드를 방문한 후 레벨 `1`로 간다. 그리고 레벨`1`에 있는 모든 노드를 방문한 후 레벨`2`로 간다. ...   이런 과정을 말단 레벨까지 반복하게 된다. BFS로 어떻게 특정 노드의 레벨을 구할 수 있을까?



BFS의 기본적인 알고리즘은 다음과 같다.

1. 큐에서 노드 `cur`를 꺼낸다.
2. `cur`의 인접 노드들 중 아직 큐에 넣은 적 없는 (방문한 적 없는) 노드 `nxt`들을 찾는다.
   1. 노드 `nxt`에 방문했음을 표시한다.
   2. 노드 `nxt`를 큐에 넣는다.
3. 큐가 빌 때까지 반복한다.

코드는 다음과 같다.



```python
# queue : deque
while queue:
    cur = queue.popleft()
    
    for nxt in graph[cur]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            queue.append(nxt)
```

`cur`과 `nxt`사이의 거리는 `1`이다. `cur`과 `nxt`는 인접하기 때문이다. 즉 `nxt`의 레벨은 `cur`의 레벨에 `1`을 더한 것이다. 

```python
# queue : deque
# level = [0] * N
while queue:
    cur = queue.popleft()
    
    for nxt in graph[cur]:
        if visited[nxt] == 0:
            level[nxt] = level[cur] + 1
            visited[nxt] = 1
            queue.append(nxt)
```

`level[v]`는 노드 `v`의 레벨을 나타내게 된다



## 전체 코드

```python
from collections import deque

def bfs(root: int)->None:
    queue = deque([root])
    visited[root] = 1
    
    while queue:
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                level[nxt] = level[cur] + 1
                visited[nxt] = 1
                queue.append(nxt)
                
if __name__ == '__main__':
    graph = {
        0: [1,2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1, 6],
        4: [1],
        5: [2],
        6: [3]
    }
    N = (정점의 개수)
    visited = [0] * N
    level = [0] * N
    bfs(0)
    print(level) # [0, 1, 1, 2, 2, 2, 3]
```



### `visited` 배열 사용안하기

```python
def bfs(root: int) -> None:
    queue = deque([root])
    level([root]) = 1
    
    while queue:
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            if level[nxt] == 0:
                level[nxt] = level[cur] + 1
                queue.append(nxt)
                
bfs(0)
print(level) # [1, 2, 2, 3, 3, 3, 4]
```

이 경우 루트의 레벨이 `0`이 아니라 `1`부터 시작한다. `0`부터 시작하게 하고 싶다면 `level` 배열의 요소들은 절대 나올 수 없는 임의의 수(음수나 아주 큰 수) `x`로 초기화하고 `level[root]`는 `0`으로 초기화한 후, `level[nxt] == x`로 방문했는지 (거리를 계산했는지)를 알 수 있다. 상황에 따라 사용하도록 한다.



### 두 노드 사이의 최단거리 구하기

BFS 로 가중치가 없는 그래프에서 두 노드 사이의 최단거리를 구할 수 있다.

#### 노드의 레벨과 최단거리

`노드의 레벨 구하기`에서 보았다시피, 어떤 노드 `v`의 레벨이 `k (k>=0)`라면 루트 노드부터 `v`까지 간선의 개수는 `k`이다. 이는 가중치가 없는 그래프에서 루트 노드부터 노드 `v`까지의 `최단거리`를 의미한다. (가중치가 모두 같은 그래프에서는 루트부터 `v`까지의 최단거리는 `k * 가중치`가 된다.)



#### 두 노드 사이의 최단거리

`노드의 레벨 구하기` 에서 `bfs(root)`를 호출하여 임의의 노드 `i`의 레벨 정보를 `level[i]`에 담았다. 그렇다면 임의의 서로 다른 노드 `v`와 `w` 사이의 최단 거리는 `bfs(v)`를 호출한 후 `level[w]`에 담기게 된다.
import sys
input = sys.stdin.readline

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]

def dfs(sy, sx):
    stack = []
    stack.append((sy, sx))

    while stack:
        cy, cx = stack.pop()
        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < H and 0 <= nx < W:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    stack.append((ny,nx))
    return True
    
        


if __name__ == '__main__': 
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        graph = [[0] * W for _ in range(H)]      
        for y in range(H):
            graph[y] = list(map(int, input().split()))
        result = 0
        for y in range(H):
            for x in range(W):
                if graph[y][x] == 1:
                    graph[y][x] = 0
                    result += int(dfs(y,x))
        print(result)
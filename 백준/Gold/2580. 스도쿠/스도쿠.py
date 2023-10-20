import sys
input = sys.stdin.readline

def checkRow(x, a):
    for i in range(9):
        if a == graph[i][x]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[y][i]:
            return False
    return True

def checkRect(y, x, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[ny+i][nx+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        y = blank[idx][0]
        x = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(y, x, i):
            graph[y][x] = i
            dfs(idx+1)
            graph[y][x] = 0

if __name__=='__main__':
    graph = []
    blank = []

    for i in range(9):
        graph.append(list(map(int, input().split())))

    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                blank.append((i, j))
    dfs(0)

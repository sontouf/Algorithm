import sys
input = sys.stdin.readline

def checkRow(x, num): # 현재 x 에 해당하는 row에 i가 있나요
    for i in range(9):
        if board[i][x] == num:
            return False
    return True

def checkColumn(y, num): # 현재 y 에 해당하는 column에 i가 있나요
    for i in range(9):
        if board[y][i] == num:
            return False
    return True

def checkRect(x, y, num): # 현재 x ,y 에 해당하는 3*3 사각형에 i가 있나요
    sy, sx = (y// 3) * 3, (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[i+sy][j+sx] == num:
                return False
    return True
    

def dfs(n): # n번째 빈칸 해결
    if n == len(blank):
        for i in range(9):
            print(*board[i], sep='')
        exit(0)
    for i in range(1,10): # 현재 i 라는 숫자 넣어보기
        y, x = blank[n][0], blank[n][1]
        if checkRow(x, i) and checkColumn(y, i) and checkRect(x, y, i):
            board[y][x] = i
            dfs(n+1)
            board[y][x] = 0

if __name__=='__main__':
    board = [list(map(int, input().strip())) for _ in range(9)]
    blank = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blank.append((i,j))
    dfs(0)
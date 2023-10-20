import sys
input = sys.stdin.readline

def checkQueen(row):
    for i in range(row):
        if board[row] == board[i] or abs(board[row] - board[i]) == row - i:
            return False
    return True



def nqueen(row):
    global count
    if row == N:
        count += 1
        return
    else:
        for i in range(N):
            board[row] = i
            if checkQueen(row):
                nqueen(row+1)






if __name__=='__main__':
    N = int(input())
    count = 0
    board = [0] * N 
    nqueen(0)
    print(count)
    
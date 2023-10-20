import sys
input = sys.stdin.readline

if __name__=='__main__':
    N = int(input())
    count = 0
    while True:
        if N < 0:
            break
        if N % 5 == 0:
            break
        N = N - 3
        count += 1 
    if N % 5 == 0:
        print(count + N // 5)
    else:
        print(-1)
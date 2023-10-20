import sys
input = sys.stdin.readline

def fibo(n, parse):
    temp = 0
    fibo_1 = int(not(0 ^ parse))
    fibo_2 = int(not(1 ^ parse))
    if n == 0:
        return fibo_1
    elif n == 1:
        return fibo_2
    elif n >= 2:
        for _ in range(n-1):
            temp = fibo_2
            fibo_2 = fibo_1 + fibo_2
            fibo_1 = temp
        return fibo_2
if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        num = int(input())
        print(fibo(num, 0), fibo(num, 1))


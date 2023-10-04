import math

if __name__=='__main__':
    N, M = map(int, input().split())
    print(math.comb(N-1, M-1))
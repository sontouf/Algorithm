def program(N, r ,c):
    if N == 1:
        return r*2+c
    half = 1 << (N-1)
    full = half << 1
    if 0 <= r < half:
        if 0 <= c < half:
            return program(N - 1, r, c)
        elif half <= c < full:
            return half*half + program(N - 1, r, c - half)
    elif half <= r < full:
        if 0 <= c < half:
            return 2 * half * half + program(N - 1,r - half, c)
        elif half <= c < full:
            return 3 * half * half + program(N - 1,r - half, c - half)
    
    

if __name__=='__main__':
    N,r,c=map(int, input().split())
    print(program(N, r ,c))
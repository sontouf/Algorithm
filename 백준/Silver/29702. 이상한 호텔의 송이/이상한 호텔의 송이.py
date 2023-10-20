T = int(input())
for _ in range(T):
    N = int(input()) # 6
    bin_l = len(bin(N)[2:])
    if bin_l == 1:
        bin_N = '1'
    else:
        bin_N = bin(N)[3:]
    room_num = 1
    for i in range(bin_l):
        room_num = int(bin_N,2)+1
        result = str(room_num).zfill(18)
        print(bin_l-i, result, sep='')
        bin_N = int(bin_N,2)
        bin_N >>= 1
        bin_N = bin(bin_N)[2:]

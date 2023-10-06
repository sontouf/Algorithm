S, M = map(int, input().split())
if S > 1023:
    total = S - 1023 # 무조건 양수
    if total < M:
        bin_m = bin(M)[2:] # 있는 돈
        bin_total = bin(total)[2:].zfill(len(bin_m)) # 필요한 돈
    else:
        bin_total = bin(total)[2:] # 필요한 돈
        bin_m = bin(M)[2:].zfill(len(bin_total)) # 있는 돈
    for b_m, b_t in zip(bin_m, bin_total):
        if b_m == '0' and b_t == '1':
            print("Impossible")
            exit(0)
    print("Thanks")
else:
    print("No thanks")
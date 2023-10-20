def plus_one(bin_num):
    temp = 1
    result = []
    
    for bi_idx, bi in enumerate(bin_num[::-1]):
#         print(f"bi - {bi}")
        plus_result = int(bi) + temp
#         print(f"plus_result - {plus_result}")
        
        if plus_result > 1:
            result.append("0")
        else:
            result.append("1")
            temp = 0

        if temp == 0:
            break
            
    return bin_num[:32-bi_idx-1] + result[::-1]



N = int(input())
n_32bit = list(bin(N)[2:].zfill(32))
n_32bit_complement = [str(abs(int(bi)-1)) for bi in n_32bit]
complement = plus_one(n_32bit_complement)
answer = 0
for bi, co in zip(n_32bit, complement):
        if bi != co:
            answer += 1
print(answer)
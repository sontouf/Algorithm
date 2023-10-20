import sys
input = sys.stdin.readline    

if __name__=='__main__':
    dp = [0]*16
    number1 = list(map(int, input().strip()))
    number2 = list(map(int, input().strip()))
    for i in range(16):
        if i % 2 == 0:
            dp[i] = number1[i // 2]
        else:
            dp[i] = number2[(i-1)//2]
    for _ in range(14):
        for i in range(15):
            dp[i] = (dp[i] + dp[i+1]) % 10
    print(dp[0], dp[1], sep='')
    
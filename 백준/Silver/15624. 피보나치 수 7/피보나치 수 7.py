if __name__=='__main__':
    N = int(input())
    num1 = 0
    num2 = 1
    for i in range(N-1):
        num1, num2 = num2 % 1000000007, (num1+num2)%1000000007
    print(num2)
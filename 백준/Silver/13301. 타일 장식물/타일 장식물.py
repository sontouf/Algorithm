import sys
input = sys.stdin.readline

if __name__=='__main__':
    N = int(input())
    N += 2
    num1 = 1
    num2 = 1
    temp = 0
    while N != 2:
        N -= 1
        temp = num2
        num2 = num1 + num2
        num1 = temp
    print(num2 << 1)

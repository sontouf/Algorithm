import sys
input = sys.stdin.readline

if __name__=='__main__':
    i = int(input())
    j = i-1
    num1 = 0
    num2 = 1
    temp = 0
    while j != 0:
        j -= 1
        temp = num2
        num2 = num1 + num2
        num1 = temp
    print(num2, i-2, sep=' ')
    
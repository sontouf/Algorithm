import sys

input = sys.stdin.readline

def program(s : list)->str:
    passValue = 1
    waitStack = []
    while s:
        if passValue == s[0]:
            s.pop(0)
            passValue += 1
        else:
            waitStack.append(s.pop(0))
        
        while waitStack:
            if waitStack[-1] == passValue:
                waitStack.pop()
                passValue += 1
            else:
                break
    print("Nice" if not waitStack else "Sad")
test_case = input()
program(list(map(int, input().split())))

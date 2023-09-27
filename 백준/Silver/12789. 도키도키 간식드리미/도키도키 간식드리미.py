import sys

input = sys.stdin.readline

def program(s : list)->str:
    passValue = 1 # 현재 지나가야 할 번호
    waitStack = [] # 임시 대기줄
    while s: # 대기줄이 다 끝날때까지 물어보자
        if passValue == s[0]: # 지금 대기 번호 맞으신가요?
            s.pop(0)
            passValue += 1
        else: # 아니시면 임시로 가세요
            waitStack.append(s.pop(0))
        
        # 대기번호가 최신화됐을 수 있음
        while waitStack: # 대기번호가 바뀌었는데 혹시 현재 대기번호신가요?
            if waitStack[-1] == passValue:
                waitStack.pop()
                passValue += 1
            else:
                break
    print("Nice" if not waitStack else "Sad") # 임시 대기줄까지 비었으면 다 통과
test_case = input()
program(list(map(int, input().split())))

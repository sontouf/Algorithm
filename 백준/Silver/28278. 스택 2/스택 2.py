import sys

input =  sys.stdin.readline

class ListNode:
    def __init__(self, val: int, next: 'ListNode' = None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self) -> int:
        return 1 if self.top is None else 0
    
    def push(self, item: int):
        self.top = ListNode(item, self.top)
        self.count += 1

    def pop(self) -> int:
        if self.is_empty():
            return -1
        val = self.top.val
        self.top = self.top.next
        self.count -= 1

        return val
    
    def peek(self) -> int:
        return -1 if self.is_empty() else self.top.val
    
    def countItem(self) -> int:
        return self.count

def program(stack: Stack, input: str):
    if input[0] == '1':
        stack.push(input[1])
    elif input[0] == '2':
        print(stack.pop())
    elif input[0] == '3':
        print(stack.countItem())
    elif input[0] == '4':
        print(stack.is_empty())
    elif input[0] == '5':
        print(stack.peek())

stack = Stack()
for _ in range(int(input())):
    program(stack, list(input().strip().split()))
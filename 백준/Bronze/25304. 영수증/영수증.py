import sys
input = sys.stdin.readline

total = int(input().strip())
case = int(input().strip())
for _ in range(case):
    a, b = map(int, input().split())
    total -= a*b

print("Yes" if total == 0 else "No")
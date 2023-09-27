import sys

input = sys.stdin.readline
a = []
case = int(input())
for _ in range(case):
    a.append(int(input()))

a.sort()
for i in range(case):
    print(a[i])

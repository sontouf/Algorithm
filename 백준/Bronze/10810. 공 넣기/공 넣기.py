import sys
input = sys.stdin.readline
arr_size, case= map(int, input().split())
arr = [0] * arr_size
for _ in range(case):
    start, end, num_ball = map(int, input().split())
    for i in range(start, end+1):
        arr[i-1] = num_ball

print(*arr)
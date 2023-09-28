import sys
input = sys.stdin.readline

arr_size, case = map(int, input().split())
arr = [0] * arr_size
for i in range(arr_size):
    arr[i] = i+1
for _ in range(case):
    first, second = map(int, input().split())
    arr[first-1], arr[second-1] = arr[second-1], arr[first-1]
print(*arr)
case = input()
s = list(map(int, input().split()))
tag = int(input())
count = 0
for i in s:
    if (tag == i):
        count += 1
print(count)
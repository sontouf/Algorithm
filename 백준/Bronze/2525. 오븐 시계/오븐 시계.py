a, b = list(map(int, input().split()))
c = int(input())
if b+c >= 60:
    d = (b+c)%60
    a += (b+c)//60
else:
    d = b+c
if a >= 24:
    a -= 24
print(a, d)
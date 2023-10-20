numbers = list(map(int, input().split()))
ret = 0
if numbers[0] == numbers[1] == numbers[2]:
    ret = 10000 + numbers[0] * 1000
elif numbers[0] == numbers[1]:
    ret = 1000 + numbers[0] * 100
elif numbers[1] == numbers[2]:
    ret = 1000 + numbers[1] * 100
elif numbers[0] == numbers[2]:
    ret = 1000 + numbers[0] * 100
else:
    numbers.sort(reverse=True)
    ret = numbers[0] * 100  
print(ret)
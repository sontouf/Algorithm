target = list(map(int, input().split()))
reward = list(map(int, input().split()))
reward.sort()
print(reward[-target[1]])
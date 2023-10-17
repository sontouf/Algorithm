import sys
from collections import deque
input = sys.stdin.readline

if __name__=='__main__':
	N = int(input())
	arr = deque(map(int, input().split()))
	younghak = [0]
	count = 0
	while arr:
		cur = arr.popleft()
		if younghak[0] == cur:
			count += 1
			younghak[0] += 1
			if younghak[0] == 3:
				younghak[0] = 0
	print(count)
		
import sys
input = sys.stdin.readline

def attack(start):
	for i in range(start, N):
		a[i+1] = min(b[i], c[i]) + 1
		if firstfloor[i] + secondfloor[i] <= W:
			a[i+1] = min(a[i+1], a[i] + 1)
		if i > 0 and firstfloor[i-1] + firstfloor[i] <= W and secondfloor[i-1] + secondfloor[i] <= W:
			a[i+1] = min(a[i+1], a[i-1] + 2)
		if i < N - 1:
			b[i+1] = a[i+1]+1
			if firstfloor[i] + firstfloor[i+1] <= W:
				b[i+1] = min(b[i+1], c[i] + 1)
			
			c[i+1] = a[i+1]+1
			if secondfloor[i] + secondfloor[i+1] <= W:
				c[i+1] = min(c[i+1], b[i] + 1)

if __name__=='__main__':
	T = int(input())
	result_list = []
	for _ in range(T):
		N, W = map(int, input().split())
		firstfloor = list(map(int, input().split()))
		secondfloor = list(map(int, input().split()))
		a = [0 for _ in range(N + 1)]
		b = [0 for _ in range(N + 1)]
		c = [0 for _ in range(N + 1)]

		a[0] = 0
		b[0] = 1
		c[0] = 1
		attack(0)
		result = a[N]

		if N > 1 and firstfloor[0] + firstfloor[N-1] <= W:
			a[1] = 1
			b[1] = 2
			c[1] = 2
			if secondfloor[0] + secondfloor[1] <= W:
				c[1] = 1
			attack(1)
			result = min(result, c[N-1] + 1)

		if N > 1 and secondfloor[0] + secondfloor[N-1] <= W:
			a[1] = 1
			c[1] = 2
			b[1] = 2
			if firstfloor[0] + firstfloor[1] <= W:
				b[1] = 1
			attack(1)
			result = min(result, b[N-1] + 1)

		if N > 1 and firstfloor[0] + firstfloor[N-1] <= W and secondfloor[0] + secondfloor[N-1] <= W:
			a[1] = 0
			b[1] = 1
			c[1] = 1
			attack(1)
			result = min(result, a[N-1] + 2)

		result_list.append(result)
	print(*result_list,sep='\n')

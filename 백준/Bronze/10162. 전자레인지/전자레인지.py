import sys
input = sys.stdin.readline

if __name__=='__main__':
	N = int(input())
	if N % 10 != 0:
		print(-1)
		exit(0)
	arr = [300, 60, 10]
	for i in arr:
		print(N // i, end = ' ')
		N %= i
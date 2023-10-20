import sys
input = sys.stdin.readline

def f(total):
	arr = [25, 10 ,5, 1]
	for i in arr:	
		print(total // i, end = ' ')
		total %= i

if __name__=='__main__':
	T = int(input())
	for _ in range(T):
		f(int(input()))
		print()
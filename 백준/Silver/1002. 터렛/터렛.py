import sys
import math
input = sys.stdin.readline

if __name__=='__main__':
	T = int(input())
	for _ in range(T):
		x1, y1, r1, x2, y2, r2 = map(int, input().split())
		if r1 == r2 and x1 == x2 and  y1 == y2:
			print(-1)
		else:
			point = [tuple((x1,y1,r1)), tuple((x2,y2,r2))]
			point.sort(key=lambda x: x[2])
			d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
			small = point[0][2]
			large = point[1][2]
			if large > d:
				if d + small < large:
					print(0)
				elif d + small == large:
					print(1)
				elif d + small > large:
					print(2)
			elif large < d:
				if d < large + small:
					print(2)
				elif d == large + small:
					print(1)
				elif d > large + small:
					print(0)
			else:
				print(2)
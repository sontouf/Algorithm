x1, y1, x2, y2, x3, y3 = map(int, input().split())

if ((x1-x2)*(y1-y3) == (x1-x3)*(y1-y2)):
	print(-1.0)
	exit(0)
l_1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
l_2 = ((x2-x3)**2 + (y2-y3)**2)**0.5
l_3 = ((x3-x1)**2 + (y3-y1)**2)**0.5

result = 2 * max(abs(l_1-l_2), abs(l_2-l_3), abs(l_3-l_1))
print(result)
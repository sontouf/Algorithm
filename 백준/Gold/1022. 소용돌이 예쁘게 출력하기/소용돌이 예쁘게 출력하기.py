import sys
input = sys.stdin.readline

def printvalue(i, j):
	if i == j and i >= 0:
		return (2*i + 1) ** 2
	if j > 0 and j - 1 >= i >= -j:
		return (j*2-1)**2 + j - i
	if i < 0 and -(1+i) >= j >= i:
		return 2*i*(2*i + 1) + 1 - (j + i)
	if j < 0 and -j >= i >= 1+j:
		return (j*2+1)**2 - 5*j + i
	if i > 0 and i >= j >= 1-i:
		return (i*2-1)**2 + 7*i + j
	
def width(i ,j):
	result = printvalue(i, j)
	temp = result
	count = 0
	while temp:
		count += 1
		temp = temp // 10
	return (count, result)


def whitespace(i, j):
	cur_width, result = width(i, j)
	temp = max_width - cur_width
	while temp:
		temp -= 1
		print(' ', end='')
	print(result, end='')

if __name__=='__main__':
	max_width = 0
	r1, c1, r2, c2 = map(int, input().split())
	for i in range(r1, r2+1):
		for j in range(c1, c2+1):
			cur_width, temp = width(i, j)
			max_width = max(max_width, cur_width)

	for i in range(r1, r2):
		for j in range(c1, c2):
			whitespace(i, j)
			print(' ', end = '')
		whitespace(i ,c2)
		print()
	for j in range(c1, c2):
		whitespace(r2, j)
		print(' ', end='')
	whitespace(r2, c2)

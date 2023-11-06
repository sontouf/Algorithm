import sys
from collections import deque
input = sys.stdin.readline

dy = [0,0,-1,1,1,1,-1,-1]
dx = [-1,1,0,0,1,-1,1,-1]

if __name__=='__main__':
	K_p, E_p, N = input().split()
	command = deque()
	for _ in range(int(N)):
		cur = input().strip()
		if cur == "L":
			command.append(0)
		elif cur == "R":
			command.append(1)
		elif cur == "B":
			command.append(2)
		elif cur == "T":
			command.append(3)
		elif cur == "RT":
			command.append(4)
		elif cur == "LT":
			command.append(5)
		elif cur == "RB":
			command.append(6)
		elif cur == "LB":
			command.append(7)
	cx_K, cy_K = ord(K_p[0]), ord(K_p[1])
	cx_E, cy_E = ord(E_p[0]), ord(E_p[1])
	while command:
		cur = command.popleft()
		nx_K, ny_K = dx[cur] + cx_K, dy[cur] + cy_K
		if 65<=nx_K<=72 and 49<=ny_K<=56:
			if ny_K == cy_E and nx_K == cx_E:	
				nx_E, ny_E = dx[cur] + cx_E, dy[cur] + cy_E
				if 65<=nx_E<=72 and 49<=ny_E<=56:
					cy_E, cx_E = ny_E, nx_E
					cy_K, cx_K = ny_K, nx_K
			else:
				cy_K, cx_K = ny_K, nx_K
	print(chr(cx_K), chr(cy_K), sep='')
	print(chr(cx_E), chr(cy_E), sep='')
		
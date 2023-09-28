import sys
num_recur = 0

def recursion(s, l, r, num_recur):
    if l >= r: return [1, num_recur]
    elif s[l] != s[r]: return [0, num_recur]
    else: 
        return recursion(s, l+1, r-1, num_recur+1)

def isPalindrome(s, num_recur):
    return recursion(s, 0, len(s)-1, num_recur)

for _ in range(int(input())):
    print(*isPalindrome(sys.stdin.readline().strip(), 1))
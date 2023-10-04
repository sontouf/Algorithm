import sys
import itertools
input = sys.stdin.readline


if __name__=='__main__':
    N = int(input())
    nums = [1,5,10,50]
    result = set()
    for temp in itertools.combinations_with_replacement(range(4), N):
        total = 0
        for i in temp:
            total += nums[i]
        result.add(total)
    print(len(result))
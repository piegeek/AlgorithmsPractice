import sys
import math

def proctor():
    N, A, B, C = parse_input()
    solve_proctor(N, A, B, C)

def solve_proctor(N, A, B, C):
	ret = 0

	for i in range(N):
		ret += 1
		left = math.ceil((A[i] - B) / C)
		ret += left

	print(ret)
	return ret

def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    return N, A, B, C


# example usage
if __name__ == "__main__":
	proctor()
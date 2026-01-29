import sys

# Had help doing this problem
def loan():
    T, test_cases = parse_input()

    for N, M, P in test_cases:
        solve_loan(N, M, P)

def solve_loan(N, M, P):
	hi = N * (1 + (P / (100 * 12)))
	lo = 0

	mid = (lo + hi) / 2

	for it in range(100+1):
		mid = (lo + hi) / 2

		rem = get_remaining(N, M, P, mid)

		# C too big
		if rem < 0:
			hi = mid
		# C too small
		else:
			lo = mid

	print(hi)
	return hi

def get_remaining(N, M, P, C):
	if M == 1:
		return N * (1 + (P / (100 * 12))) - C
	tot = get_remaining(N, M-1, P, C)
	return tot * (1 + (P / (100 * 12))) - C

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # N and P are real numbers, M is an integer
        N, M, P = input().split()
        N = float(N)
        M = int(M)
        P = float(P)
        test_cases.append((N, M, P))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	loan()
import sys

def snail():
    C, test_cases = parse_input()
    for n, m in test_cases:
        print(solve_snail(n, m))

def solve_snail(n, m):
	low = n - m
	high = m

	prob_sum = 0

	while low <= high:
		prob_sum += combination(high, low) * ((0.75) ** low) * ((0.25) ** (high - low))

		low += 1

	return prob_sum

def combination(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))

def factorial(n):
	if n == 0 or n == 1: return 1
	return n * factorial(n-1)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (1 ≤ C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Well depth n and rainy period length m (1 ≤ n, m ≤ 1000)
        n, m = map(int, input().split())
        test_cases.append((n, m))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	snail()
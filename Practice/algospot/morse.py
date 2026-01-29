import sys

def morse():
    C, test_cases = parse_input()
    for n, m, k in test_cases:
        ret = []
		# Why this works when k - 1 and not when k -> jump over k-1 elements (ref: book)
        solve_morse(n, m, k-1, ret)
        print(''.join(ret))

def solve_morse(n, m, k, ret):
	long_signal = '-'
	short_signal = 'o'

	if n == 0 and m != 0:
		for _ in range(m):
			ret.append(short_signal)
		return

	if n != 0 and m == 0:
		for _ in range(n):
			ret.append(long_signal)
		return

	if n == 0 and m == 0:
		return

	boundary = get_number_of_combinations_with_duplicates(n-1, m)

	# (-) comes first
	if k < boundary:
		ret.append(long_signal)
		solve_morse(n-1, m, k, ret)

	# (o) comes first
	else:
		ret.append(short_signal)
		solve_morse(n, m-1, k - boundary, ret)

def get_number_of_combinations_with_duplicates(n, m):
	return factorial(n + m) / (factorial(n) * factorial(m))

def factorial(n):
	if n <= 1: return 1

	return n * factorial(n-1)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Integers n, m, k (1 ≤ n, m ≤ 100; 1 ≤ k ≤ 1,000,000,000)
        n, m, k = map(int, input().split())
        test_cases.append((n, m, k))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	morse()
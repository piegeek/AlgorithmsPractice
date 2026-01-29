import sys

# Needs fixing; subsequence doesn't need to be in sequence

def lis():
    C, test_cases = parse_input()
    for N, sequence in test_cases:
        print(solve_lis(N, sequence))

def solve_lis_consecutive(N, sequence):
	dp = [-1 for i in range(len(sequence))]

	for i in range(len(sequence) - 1):
		if sequence[i] < sequence[i+1]:
			dp[i+1] = i

	# print(dp)

	counts = []

	count = 1

	for i in range(len(dp)):
		if dp[i] == -1:
			counts.append(count)
			count = 1
		else:
			count += 1

	counts.append(count)

	return max(counts) 

def solve_lis(N, sequence):
	ret = 1

	for i in range(len(sequence)):
		if sequence[0] < sequence[i]:
			ret = max(ret, 1 + solve_lis(N, sequence[i:]))

	return ret


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of elements in the sequence (N ≤ 500)
        N = int(input().strip())

        # The sequence of N integers
        sequence = list(map(int, input().split()))
        assert len(sequence) == N

        test_cases.append((N, sequence))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	lis()

import sys
import itertools

# STAR

def quantize():
    C, test_cases = parse_input()
    for N, S, sequence in test_cases:
        print(solve_quantize(N, S, sequence))

def solve_quantize(N, S, sequence):
	sequence = sorted(sequence)

	indices = [i for i in range(N)]

	combs = itertools.combinations(indices, S-1)

	min_sq_err = float('inf')

	for comb in combs:
		sq_err = 0

		if comb[0] > 0:
			sq_err += get_sq_err(sequence[0:comb[0]])

		for i in range(len(comb)-1):
			sq_err += get_sq_err(sequence[comb[i]:comb[i+1]])

		sq_err += get_sq_err(sequence[comb[-1]:])

		print(f'sq_err: {sq_err}, comb: {comb}')

		min_sq_err = min(min_sq_err, sq_err)

	return min_sq_err

def get_sq_err(sequence):
	average = int(sum(sequence) / len(sequence)) 

	sq_err = 0
	sq_err2 = 0

	for s in sequence:
		sq_err += (s - average) ** 2
		sq_err2 += (s - (average + 1)) ** 2

	return min(sq_err, sq_err2)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (1 ≤ C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Length of the sequence N and number of usable numbers S
        N, S = map(int, input().split())

        # Sequence of N integers
        sequence = list(map(int, input().split()))
        assert len(sequence) == N

        test_cases.append((N, S, sequence))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	quantize()

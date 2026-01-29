import sys

def lunchbox():
    T, test_cases = parse_input()

    for N, M, E in test_cases:
        solve_lunchbox(N, M, E)

def solve_lunchbox(N, M, E):
	indices = [i for i in range(N)]
	combs = choose_two(indices)

	ret = float('inf')

	for comb in combs:
		first, last = comb[0], comb[1]

		# If E1 + E2 < M2 + M3; eating time shorter
		microwaving_time = sum([M[i] for i in range(len(M)) if i != first])

		# If E1 + E2 >= M2 + M3; eating time longer
		eating_time = sum([E[i] for i in range(len(E)) if i != last])

		ret = min(
			ret,
			M[first] + microwaving_time + E[last],
			M[first] + microwaving_time + E[last]
		)

		first, last = comb[1], comb[0]

		# If E1 + E2 < M2 + M3; eating time shorter
		microwaving_time = sum([M[i] for i in range(len(M)) if i != first])

		# If E1 + E2 >= M2 + M3; eating time longer
		eating_time = sum([E[i] for i in range(len(E)) if i != last])

		ret = min(
			ret,
			M[first] + microwaving_time + E[last],
			M[first] + microwaving_time + E[last]
		)

	print(ret)


def choose_two(indices):
	combs = []

	for i in range(len(indices)):
		for j in range(i, len(indices)):
			combs.append([i, j])

	return combs

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # Number of participants
        N = int(input().strip())

        # M1, M2, ..., MN
        M = list(map(int, input().split()))
        assert len(M) == N

        # E1, E2, ..., EN
        E = list(map(int, input().split()))
        assert len(E) == N

        test_cases.append((N, M, E))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	lunchbox()
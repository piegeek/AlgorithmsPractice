import sys

def withdrawal():
    T, test_cases = parse_input()

    for n, k, subjects in test_cases:
        solve_withdrawal(n, k, subjects)

def solve_withdrawal(n, k, subjects):
	removed = [ False for _ in range(n) ]

	cache = {}

	ret = min_rank(0, removed, n, k, subjects, cache)

	print(ret)
	return ret

def min_rank(idx, removed, n, k, subjects, cache):
	removed_state = get_state(removed)

	if (idx, removed_state) in cache: return cache[(idx, removed_state)]
	
	# Leaf node
	if idx == n or n - removed.count(True) == k:
		unremoved_indices = [ i for i in range(n) if removed[i] == False ]

		sum_ri = 0
		sum_ci = 0

		for ui in unremoved_indices:
			sum_ri += subjects[ui][0]
			sum_ci += subjects[ui][1]

		cache[(idx, removed_state)] = sum_ri / sum_ci
		return sum_ri / sum_ci

	min_out = float('inf')

	# idx not removed
	min_out = min(
		min_out,
		min_rank(idx+1, removed, n, k, subjects, cache)
	)

	# idx removed
	removed[idx] = True

	if n - removed.count(True) >= k:
		min_out = min(
			min_out,
			min_rank(idx+1, removed, n, k, subjects, cache)
		)

	# Backtracking
	removed[idx] = False

	cache[(idx, removed_state)] = min_out
	return min_out

def get_state(removed):
	state = 0

	for i in range(len(removed)):
		if removed[i] == True:
			state |= (1 << i)

	return state

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # Number of subjects and number to keep
        n, k = map(int, input().split())

        # n pairs (ri, ci)
        pairs = list(map(int, input().split()))
        assert len(pairs) == 2 * n

        subjects = []
        for i in range(0, 2 * n, 2):
            r, c = pairs[i], pairs[i + 1]
            subjects.append((r, c))

        test_cases.append((n, k, subjects))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	withdrawal()
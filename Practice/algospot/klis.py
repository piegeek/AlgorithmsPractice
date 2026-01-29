import sys
import copy

def klis():
    C, test_cases = parse_input()
    for N, K, sequence in test_cases:
        solve_klis(N, K, sequence)

# Brute force solution first
def solve_klis(N, K, sequence):
	cache = [-1 for i in range(N)]
	choices = [-1 for i in range(N+1)]

	lis_len = get_lis(0, sequence, cache, choices)

	lises = []
	for i in range(len(sequence)):
		get_lises(i, sequence, [], lises, lis_len)

	lises = sorted(lises)

	print(lis_len)
	kth_lis = list(map(str, lises[K-1]))
	print(' '.join(kth_lis))

# If there are only two options for each subproblem a separate array to store choices is not needed
def get_lis(idx, sequence, cache, choices):
	if idx == len(sequence): 
		choices[idx+1] = 0
		cache[idx] = 0
		return 0

	if cache[idx] != -1: return cache[idx]

	lis_len = 1

	best_next = -1

	for i in range(idx+1, len(sequence)):
		if sequence[idx] < sequence[i]: 
			cand = 1 + get_lis(i, sequence, cache, choices)
			if cand > lis_len:
				lis_len = cand
				best_next = i

	choices[idx+1] = best_next
	cache[idx] = lis_len

	return lis_len

def reconstruct_lis(idx, sequence, choices):
	pass

# Leaf node case might come at the middle of function
def get_lises(idx, sequence, stack, lises, lis_len):
	# print(stack)

	stack.append(sequence[idx])

	largest_item_at_idx = True

	for i in range(idx+1, len(sequence)):
		if sequence[idx] < sequence[i]:
			# print(f'sequence[idx]: {sequence[idx]}, sequence[i]: {sequence[i]}')
			largest_item_at_idx = False
			get_lises(i, sequence, stack, lises, lis_len)

	if largest_item_at_idx:
		# print(stack)
		# Leaf node
		if len(stack) == lis_len:
			stack_copy = copy.deepcopy(stack)
			if stack_copy not in lises:
				lises.append(stack_copy)

	# Backtracking
	stack.pop(-1)

# Try like puzzle problem; force leaf node case to stay at the end
def get_lises_2(idx, sequence, stack, lises, lis_len):

	for i in range(idx+1, len(sequence)):
		if sequence[idx] < sequence[i]:
			stack.append(sequence[idx])
			get_lises(i, sequence, stack, lises, lis_len)
			# Backtracking
			stack.pop(-1)

	# Leaf node
	if len(stack) == lis_len:
		stack_copy = copy.deepcopy(stack)
		if stack_copy not in lises:
			lises.append(stack_copy)


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of elements N and integer K
        N, K = map(int, input().split())

        # Sequence of N distinct integers
        sequence = list(map(int, input().split()))
        assert len(sequence) == N

        test_cases.append((N, K, sequence))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	klis()
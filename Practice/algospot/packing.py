import sys

'''
When you feel the urge to write a for loop:

Ask: Am I exploring(yes), deciding(no), or aggregating(yes)?

DFS and for loops - am I exploring or deciding?
'''

def packing():

    C, test_cases = parse_input()
    for N, W, items in test_cases:
        print(solve_packing(N, W, items))

def solve_packing(N, W, items):
	cache = {}

	# return solve_packing_dfs(0, W, items, cache)
	# return solve_packing_dfs_2(0, W, items, cache)
	# return solve_packing_dfs_3(0, W, items, cache)
	return solve_packing_dfs_new(0, W, items, cache)

# Key takeaway - 'for loops are safe when your state defines what’s left, not just where you are.'
def solve_packing_dfs(idx, left_weight, items, cache):
	print(f'idx: {idx}, left_weight: {left_weight}')

	# Memoization
	if (idx, left_weight) in cache.keys():
		return cache[(idx, left_weight)]

	# Leaf node
	if left_weight < 0: return []

	cant_add_more = True

	for i in range(idx+1, len(items)):
		if items[i][1] <= left_weight:
			cant_add_more = False
			break

	if cant_add_more:
		max_urgency_idx = idx
		max_urgency = items[max_urgency_idx][2]

		for i in range(idx+1, len(items)):
			if items[i][2] > max_urgency:
				max_urgency_idx = i
				max_urgency = items[i][2]

		cache[(idx, left_weight)] = [items[max_urgency_idx]]

		return [items[max_urgency_idx]]

	max_urgency_sum = 0

	# With first
	for i in range(idx+1, len(items)):
		maximizing_items = solve_packing_dfs(i, left_weight - items[idx][1] - items[i][1], items, cache)

		compare_sum = 0

		for item in maximizing_items:
			compare_sum += item[2]

		compare_sum += items[idx][2]

		if compare_sum > max_urgency_sum:
			max_urgency_sum = compare_sum
			ret = maximizing_items + [items[idx]]

	# Without first
	for i in range(idx+1, len(items)):
		maximizing_items = solve_packing_dfs(i, left_weight - items[i][1], items, cache)

		compare_sum = 0

		for item in maximizing_items:
			compare_sum += item[2]

		if compare_sum > max_urgency_sum:
			max_urgency_sum = compare_sum
			ret = maximizing_items

	cache[(idx, left_weight)] = ret
	return ret

def solve_packing_dfs_new(idx, left_weight, items, cache):
	# Leaf node; base case
	if left_weight < 0: return float('-inf')
	if idx == len(items) : return 0

	# Why setting 'max_urgency = 0' works when 'items[idx][2]' doesn't -> max_urgency = items[idx][2] means I already took the item at index
	# max_urgency = items[idx][2]
	max_urgency = 0

	# For loop doens't make sense since it doesn't correspond with the subproblem I'm trying to solve; it jumps to another problem
	for i in range(idx+1, len(items)+1):
		max_urgency = max(max_urgency, items[idx][2] + solve_packing_dfs_new(i, left_weight - items[idx][1], items, cache))

	for i in range(idx+1, len(items)+1):
		max_urgency = max(max_urgency, solve_packing_dfs_new(i, left_weight, items, cache))

	return max_urgency


def solve_packing_dfs_2(idx, left_weight, items, cache):
	if left_weight < 0:
		# return 0 <- needs to be worse than 0; must invalidate path
		return float('-inf')

	# Incorrect; path always includes last item
	# if idx == len(items) - 1:
	# 	return items[idx][2]
	
	if idx == len(items):
		return 0

	# With item at idx
	max_urgency = items[idx][2] + solve_packing_dfs_2(idx + 1, left_weight - items[idx][1], items, cache)

	# Without item at idx
	max_urgency = max(max_urgency, solve_packing_dfs_2(idx+1, left_weight, items, cache))

	return max_urgency	


def solve_packing_dfs_3(idx, left_weight, items, cache):
	# Base cases
    if idx == len(items) or left_weight == 0:
        return 0

    # Option 1: skip item i
    best = solve_packing_dfs_3(idx + 1, left_weight, items, cache)

    # Option 2: take item i (if it fits)
    if items[idx][1] <= left_weight:
        best = max(
            best,
            solve_packing_dfs_3(idx + 1, left_weight - items[idx][1], items, cache) + items[idx][2]
        )

    return best
	


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (1 ≤ C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of items N and carrier capacity W
        N, W = map(int, input().split())

        items = []
        for _ in range(N):
            # Item name, volume, urgency
            name, volume, urgency = input().split()
            volume = int(volume)
            urgency = int(urgency)
            items.append((name, volume, urgency))

        test_cases.append((N, W, items))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	packing()
import sys

def tripathcnt():
    C, test_cases = parse_input()
    for n, triangle in test_cases:
        print(solve_tripathcnt(n, triangle))

def solve_tripathcnt(n, triangle):
	directions = [
		[1, 0],
		[1, 1]
	]

	# Count should start at 1; count of any path should start at 1
	count = [1]
	max_length = [0]
	stack = []

	dfs(n, triangle, 0, 0, directions, 0, max_length, count, stack)

	return count[0]

def dfs(n, triangle, i, j, directions, length, max_length, count, stack):
	curr_length = length + triangle[i][j]

	# Leaf node; base case
	if i == n-1:
		if curr_length == max_length[0]:
			count[0] += 1
		elif curr_length > max_length[0]:
			max_length[0] = curr_length
			count[0] = 1
		
		return

	stack.append(triangle[i][j])

	for direction in directions:
		dy, dx = direction[0], direction[1]

		if i + dy in range(n) and j + dx in range(n):
			dfs(n, triangle, i+dy, j+dx, directions, curr_length, max_length, count, stack)

	# Backtracking
	stack.pop(-1)
		

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Size of the triangle (2 ≤ n ≤ 100)
        n = int(input().strip())

        triangle = []
        for i in range(1, n + 1):
            row = list(map(int, input().split()))
            assert len(row) == i
            triangle.append(row)

        test_cases.append((n, triangle))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	tripathcnt()
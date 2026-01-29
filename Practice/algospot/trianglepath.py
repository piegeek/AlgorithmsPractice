import sys

def trianglepath():
    C, test_cases = parse_input()
    for n, triangle in test_cases:
        print(solve_trianglepath(n, triangle))

def solve_trianglepath(n, triangle):
	moves = [
		[1, 0],
		[1, 1]
	]

	max_sum = [ [ 0 for col in row ] for row in triangle ]

	visited = [ [ False for col in row ] for row in triangle ]

	dfs(triangle, 0, 0, max_sum, visited, moves, 0)

	return max(max_sum[-1])

def dfs(triangle, i, j, max_sum, visited, moves, curr_sum):
	if visited[i][j]: return

	# Pruning
	if curr_sum + triangle[i][j] <= max_sum[i][j]: return

	visited[i][j] = True

	new_sum = curr_sum + triangle[i][j]

	max_sum[i][j] = new_sum

	move1 = moves[0]
	move2 = moves[1]

	r1, c1 = i + move1[0], j + move1[1]
	r2, c2 = i + move2[0], j + move2[1]

	if r1 <= len(triangle) - 1 and c1 <= len(triangle[r1]) - 1:
		dfs(triangle, r1, c1, max_sum, visited, moves, new_sum)

	if r2 <= len(triangle) - 1 and c2 <= len(triangle[r2]) - 1:
		dfs(triangle, r2, c2, max_sum, visited, moves, new_sum)

	# Backtracking
	visited[i][j] = False

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


if __name__ == "__main__":
	trianglepath()
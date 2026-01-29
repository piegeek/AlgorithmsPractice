import sys
import copy
import math

def minastirith():
    c, test_cases = parse_input()

    for n, posts in test_cases:
        solve_minastirith(n, posts)

def solve_minastirith(n, posts):
	cache = {}
	visited = 0

	# Make Covered
	covered = []
	for x in range(-8, 8+1):
		for y in range(int(-math.sqrt(64 - x**2)), int(math.sqrt(64 - x**2))):
			covered.append([x, y, 0])

	for i in range(len(posts)):
		for j in range(len(covered)):
			if inside_circle(
				covered[j][0],
				covered[j][1],
				posts[i][1],
				posts[i][0],
				posts[i][2]
			):
				covered[j][2] += 1

	ret = min_posts(0, visited, n, covered, posts, cache)

	print(ret)
	
	return ret

def min_posts(idx, visited, n, covered, posts, cache):
	# Leaf node
	if idx == n or (visited == ((1 << n) - 1)): return 0

	if (idx, visited) in cache: return cache[(idx, visited)]

	min_num = float('inf')

	# Keep posts[idx]
	min_num = min(
		min_num,
		1 + min_posts(idx+1, visited, n, covered, posts, cache)
	)

	# Remove posts[idx]
	visited |= (1 << idx)

	can_remove = True

	for j in range(len(covered)):
		if inside_circle(
				covered[j][0],
				covered[j][1],
				posts[idx][1],
				posts[idx][0],
				posts[idx][2]
			):

			covered[j][2] -= 1

			if covered[j][2] == 0:
				can_remove = False

	if can_remove:
		min_num = min(
			min_num,
			min_posts(idx+1, visited, n, covered, posts, cache)
		)

	# Backtracking
	for j in range(len(covered)):
		if inside_circle(
				covered[j][0],
				covered[j][1],
				posts[idx][1],
				posts[idx][0],
				posts[idx][2]
			):

			covered[j][2] += 1

	cache[(idx, visited)] = min_num
	return min_num

def inside_circle(x, y, a, b, r):
	return (x-a) ** 2 + (y-b) ** 2 <= r ** 2

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Number of guard posts
        n = int(input().strip())

        posts = []
        for _ in range(n):
            y, x, r = map(float, input().split())
            posts.append((y, x, r))

        test_cases.append((n, posts))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	minastirith()
import sys
import heapq

def minastirith():
    c, test_cases = parse_input()

    for n, posts in test_cases:
        solve_minastirith_dfs(n, posts)

def solve_minastirith(n, posts):
	midpoints = []

	for post in posts:
		y, x, r = post
		midpoints.append(get_midpoint([0,0], [x,y]))

	queue = []

	for i in range(len(posts)):
		b, a, r = posts[i]
		heapq.heappush(queue, [[i], [[a, b, r]]])

	while len(queue) > 0:
		checked_indices, points = heapq.heappop(queue)

		if can_cover_all(midpoints, points):
			print(len(points))
			return

		unchecked_indices = [ i for i in range(len(posts)) if i not in checked_indices ]

		for idx in unchecked_indices:
			b_new, a_new, r_new = posts[idx]
			new_post = [a_new, b_new, r_new]
			heapq.heappush(queue, [checked_indices + [idx], points + [new_post]])

def solve_minastirith_dfs(n, posts):
	if len(posts) == 1:
		if posts[0][2] < 16:
			return -1

	midpoints = []

	for post in posts:
		y, x, r = post
		midpoints.append(get_midpoint([0,0], [x,y]))

	can_remove = 0

	# 0 needed
	if not can_cover_all(midpoints, posts[1:]):
		can_remove = max(can_remove, dfs(0, posts, midpoints))

	# 0 not needed
	else:
		can_remove = max(can_remove, 1 + dfs(1, posts, midpoints))

	print(n - can_remove)

def dfs(idx, posts, midpoints):
	if idx == len(posts):
		return 0

	can_remove = 0

	# idx+1 needed
	if not can_cover_all(midpoints, posts[:idx+1] + posts[idx+2:]):
		can_remove = max(can_remove, dfs(idx+1, posts, midpoints))

	# idx+1 not needed
	else:
		can_remove = max(can_remove, 1 + dfs(idx+2, posts, midpoints))

	return can_remove


def can_cover_all(midpoints, points):
	for midpoint in midpoints:
		for point in points:
			# print(points)
			a, b, r = point 
			x, y = midpoint
			
			if not inside_circle(x, y, a, b, r):
				return False

	return True

def get_midpoint(coord1, coord2):
	return (coord1[0] + coord2[0]) / 2, (coord1[1] + coord2[1]) / 2

def inside_circle(x, y, a, b, r):
	return (x-a) ** 2 + (y-b) ** 2 < r ** 2

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
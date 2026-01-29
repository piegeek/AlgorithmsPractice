import sys

# Need to fix hull handling
def fossil():
    c, test_cases = parse_input()

    for n, m, hull1, hull2 in test_cases:
        solve_fossil(n, m, hull1, hull2)

def solve_fossil(n, m, hull1, hull2):
	upper = []
	lower = []

	decompose(upper, lower, hull1)
	decompose(upper, lower, hull2)

	lo = max(min_x(hull1), min_x(hull2))
	hi = min(max_x(hull1), max_x(hull2))

	print(f'lo: {lo}')
	print(f'hi: {hi}')

	if hi < lo:
		print(0)
		return 0

	for it in range(100+1):
		aab = (lo * 2 + hi) / 3
		abb = (lo + 2 * hi) / 3

		if vertical(aab, upper, lower) < vertical(abb, upper, lower):
			lo = aab
		else:
			hi = abb

	ret = max(0, vertical(hi))
	print(ret)
	return ret

def min_x(hull):
	min_x_val = hull[0]
	for i in range(int(len(hull) / 2)):
		if hull[2*i] < min_x_val:
			min_x_val = hull[2*i]

	return min_x_val

def max_x(hull):
	max_x_val = hull[1]
	for i in range(int(len(hull) / 2)):
		if hull[2*i+1] > max_x_val:
			max_x_val = hull[2*i+1]

	return max_x_val

def between(x, point_a, point_b):
	return (point_a[0] <= x and x <= point_b[0]) or (point_b[0] <= x and x <= point_a[0])

def vertical(x, upper, lower):
	min_up = float('inf')
	max_low = float('-inf')

	for i in range(len(upper)):
		if between(x, upper[i][0], upper[i][1]):
			min_up = min(min_up, get_y(upper[i][0], upper[i][1], x))

	for i in range(len(lower)):
		if between(x, lower[i][0], lower[i][1]):
			max_low = max(max_low, get_y(lower[i][0], lower[i][1], x))

	return min_up - max_low

def get_y(point_a, point_b, x):
	dx, dy = point_b[0] - point_a[0], point_b[1] - point_a[1]

	dy_dx = dy / dx

	y = dy_dx(x - point_a[0]) + point_a[1]

	return y

def decompose(upper, lower, hull):
	for i in range(int(len(hull) / 2) - 1):
		x_1 = hull[2 * i]
		y_1 = hull[2 * i + 1]

		x_2 = hull[2 * (i+1)]
		y_2 = hull[2 * (i+1) + 1]

		if x_2 < x_1:
			upper.append([[x_1, y_1], [x_2, y_2]])
		else:
			lower.append([[x_1, y_1], [x_2, y_2]])

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Number of points in each convex hull
        n, m = map(int, input().split())

        # First convex hull: 2n floats -> n (x, y) pairs
        data1 = list(map(float, input().split()))
        assert len(data1) == 2 * n
        hull1 = [(data1[i], data1[i + 1]) for i in range(0, 2 * n, 2)]

        # Second convex hull: 2m floats -> m (x, y) pairs
        data2 = list(map(float, input().split()))
        assert len(data2) == 2 * m
        hull2 = [(data2[i], data2[i + 1]) for i in range(0, 2 * m, 2)]

        test_cases.append((n, m, hull1, hull2))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	fossil()
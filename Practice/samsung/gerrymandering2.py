import sys

def gerrymandering2():
    N, A = parse_input()
    solve_gerrymandering2(N, A)

def solve_gerrymandering2(N, A):
	zones = [ [ -1 for _ in range(N) ] for _ in range(N) ]

	ret = float('inf')

	for x, y, d1, d2 in generate_points(N):
		populate_zones(N, zones, [x, y, d1, d2])
		# if (x, y, d1, d2) == (2, 4, 2, 2) or (x, y, d1, d2) == (2, 5, 3, 2) or (x, y, d1, d2) == (4, 3, 1, 1):  
		# 	print(f'x: {x}, y: {y}, d1: {d1}, d2: {d2}')
		# 	print('--------')
		# 	for row in zones:
		# 		print(row)
		# 	print('--------')

		ret = min(ret, get_pop_difference(N, A, zones))
		# Backtracking
		zones = [ [ -1 for _ in range(N) ] for _ in range(N) ]

	print(ret)
	return ret

def get_pop_difference(N, A, zones):
	pops = [ -1 for _ in range(5) ]

	for i in range(N):
		for j in range(N):
			pops[zones[i][j]-1] += A[i][j]

	return max(pops) - min(pops)

def populate_zones(N, zones, point):
	x, y, d1, d2 = point

	# 0-indexing
	x = x - 1
	y = y - 1

	# Populate 1's
	for i in range(x, x + d1 + 1):
		for j in range(0, y - (i - x)):
			zones[i][j] = 1

	# Populate 2's
	for i in range(x, x + d2 + 1):
		for j in range(y + (i - x) + 1, N):
			zones[i][j] = 2

	# Populate 3's
	for i in range(x + d1, x + d1 + d2 + 1):
		for j in range(0, y - d1 + (i - (x + d1))):
			zones[i][j] = 3

	# Populate 4's
	for i in range(x + d2, x + d2 + d1 + 1):
		for j in range(y + d2 - (i - (x + d2)) + 1, N):
			zones[i][j] = 4

	# Continue populating 
	for i in range(x-1, -1, -1):
		for j in range(0, y+1):
			zones[i][j] = 1

		for j in range(y+1, N):
			zones[i][j] = 2

	for i in range(x + d1 + d2 + 1, N):
		for j in range(y - d1 + d2):
			zones[i][j] = 3

		for j in range(y - d1 + d2, N):
			zones[i][j] = 4

	for j in range(y - d1 - 1, -1, -1):
		for i in range(0, x + d1):
			zones[i][j] = 1

		for i in range(x + d1, N):
			zones[i][j] = 3


	for j in range(y + d2 + 1, N):
		for i in range(0, x + d2 + 1):
			zones[i][j] = 2

		for i in range(x + d2 + 1, N):
			zones[i][j] = 4

	# Populate 5's
	for i in range(N):
		for j in range(N):
			if zones[i][j] == -1:
				zones[i][j] = 5
			


def generate_points(N):
	points = []
	for x in range(N):
		for y in range(N):
			for d1 in range(1, N):
				for d2 in range(1, N):
					if 1 <= x and x < x + d1 + d2 and x + d1 + d2 <= N and 1 <= y - d1 and y - d1 < y and y < y + d2 and y + d2 <= N:
						points.append([x, y, d1, d2])

	return points

def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())

    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    return N, A


# example usage
if __name__ == "__main__":
	gerrymandering2()
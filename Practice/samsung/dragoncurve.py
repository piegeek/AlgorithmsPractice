import sys

def dragoncurve():
    N, curves = parse_input()
    solve_dragoncurve(N, curves)

def solve_dragoncurve(N, curves):
	# Check if generate_dragoncurve yields correct results
	# dc0 = generate_dragoncurve(0, 0, 0, 0)
	# dc1 = generate_dragoncurve(0, 0, 0, 1)
	# dc2 = generate_dragoncurve(0, 0, 0, 2)
	# dc3 = generate_dragoncurve(0, 0, 0, 3)

	# print(dc0)
	# print(dc1)
	# print(dc2)
	# print(dc3)

	occupied = [ [ False for _ in range(100+1) ] for _ in range(100+1) ]

	for curve in curves:
		x, y, d, g = curve
		dc = generate_dragoncurve(x, y, d, g)

		for point in dc:
			r, c = point
			occupied[r][c] = True

	count = 0

	for i in range(1, 100+1):
		for j in range(1, 100+1):
			if (
				occupied[i-1][j-1] == True
				and
				occupied[i-1][j] == True
				and
				occupied[i][j-1] == True
				and
				occupied[i][j] == True
			):
				count += 1

	print(count)
	return count

def generate_dragoncurve(x, y, d, g):
	direction = [
		[0, 1],
		[-1, 0],
		[0, -1],
		[1, 0]
	]

	if g == 0:
		dy, dx = direction[d]
		return [ [y, x], [y+dy, x+dx] ]

	prev_gen_dragon_curve = generate_dragoncurve(x, y, d, g-1)

	dirs = []

	for i in range(len(prev_gen_dragon_curve) - 1):
		dirs.append(get_dir(prev_gen_dragon_curve[i], prev_gen_dragon_curve[i+1], direction))

	rot_dirs = []
	for dir in dirs:
		rot_dirs.append(rot_d_ccw(dir))

	last_from_prev_gen = prev_gen_dragon_curve[-1]
	y, x = last_from_prev_gen

	next_gen_points = []

	for i in range(len(rot_dirs) - 1, -1, -1):
		dir = rot_dirs[i]
		dy, dx = direction[dir]
		next_gen_points.append([y+dy, x+dx])
		y += dy
		x += dx

	return prev_gen_dragon_curve + next_gen_points

def get_dir(prev, next, direction):
	for d in range(len(direction)):
		if direction[d] == [ next[0] - prev[0], next[1] - prev[1] ]:
			return d

def rot_d_ccw(d):
	return (d + 1) % 4

def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())

    curves = []
    for _ in range(N):
        x, y, d, g = map(int, input().split())
        curves.append((x, y, d, g))

    return N, curves


# example usage
if __name__ == "__main__":
	dragoncurve()
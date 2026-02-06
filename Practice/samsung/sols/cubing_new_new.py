import sys

def cubing():
    T, test_cases = parse_input()

    for n, ops in test_cases:
        solve_cubing(n, ops)

def solve_cubing(n, ops):
	cube = {
		'U': [ [ 'w' for _ in range(3) ] for _ in range(3) ],
		'D': [ [ 'y' for _ in range(3) ] for _ in range(3) ],
		'F': [ [ 'r' for _ in range(3) ] for _ in range(3) ],
		'B': [ [ 'o' for _ in range(3) ] for _ in range(3) ],
		'L': [ [ 'g' for _ in range(3) ] for _ in range(3) ],
		'R': [ [ 'b' for _ in range(3) ] for _ in range(3) ]
	}

	for i in range(n):
		rotate(cube, ops[i])

	for row in cube['U']:
		print(''.join(row))

def rotate_face(cube, face, dir):
	"""face 자체를 CW 또는 CCW로 회전"""
	f = cube[face]
	if dir == '+':
		cube[face] = [
			[ f[2][0], f[1][0], f[0][0] ],
			[ f[2][1], f[1][1], f[0][1] ],
			[ f[2][2], f[1][2], f[0][2] ],
		]
	else:
		cube[face] = [
			[ f[0][2], f[1][2], f[2][2] ],
			[ f[0][1], f[1][1], f[2][1] ],
			[ f[0][0], f[1][0], f[2][0] ],
		]

def get_strip(cube, face, edge):
	"""face의 edge 방향에 해당하는 3칸 strip을 읽어온다.
	edge는 해당 면이 '위'에 있다고 봤을 때,
	회전하는 면과 맞닿는 변이 어디인지를 뜻한다.
	  'top'    -> row 0, 왼→오
	  'bottom' -> row 2, 왼→오
	  'left'   -> col 0, 위→아래
	  'right'  -> col 2, 위→아래
	"""
	if edge == 'top':
		return [cube[face][0][j] for j in range(3)]
	elif edge == 'bottom':
		return [cube[face][2][j] for j in range(3)]
	elif edge == 'left':
		return [cube[face][i][0] for i in range(3)]
	elif edge == 'right':
		return [cube[face][i][2] for i in range(3)]

def set_strip(cube, face, edge, vals):
	"""face의 edge 방향에 vals를 써넣는다."""
	if edge == 'top':
		for j in range(3):
			cube[face][0][j] = vals[j]
	elif edge == 'bottom':
		for j in range(3):
			cube[face][2][j] = vals[j]
	elif edge == 'left':
		for i in range(3):
			cube[face][i][0] = vals[i]
	elif edge == 'right':
		for i in range(3):
			cube[face][i][2] = vals[i]

def rotate(cube, op):
	face = op[0]
	dir = op[1]

	rotate_face(cube, face, dir)

	# 각 면이 회전할 때 영향받는 인접 4면과, 그 면에서 맞닿는 edge
	# CW(+) 방향 순환 순서로 나열 (strip[0] <- strip[3] <- strip[2] <- strip[1])
	# 각 항목: (인접면, edge, reverse 여부)
	# reverse=True면 strip 값을 뒤집어서 넣어야 함
	adj = {
		'U': [('B', 'top', False), ('R', 'top', False), ('F', 'top', False), ('L', 'top', False)],
		'D': [('F', 'bottom', False), ('R', 'bottom', False), ('B', 'bottom', False), ('L', 'bottom', False)],
		'F': [('U', 'bottom', False), ('R', 'left', True), ('D', 'top', False), ('L', 'right', True)],
		'B': [('U', 'top', True), ('L', 'left', False), ('D', 'bottom', True), ('R', 'right', False)],
		'L': [('U', 'left', False), ('F', 'left', False), ('D', 'left', False), ('B', 'right', True)],
		'R': [('U', 'right', True), ('B', 'left', False), ('D', 'right', True), ('F', 'right', False)],
	}

	strips_info = adj[face]

	# 4개 strip 읽기
	vals = []
	for f, edge, rev in strips_info:
		v = get_strip(cube, f, edge)
		if rev:
			v = v[::-1]
		vals.append(v)

	# CW(+): strip[i] <- strip[i-1]
	# CCW(-): strip[i] <- strip[i+1]
	if dir == '+':
		new_vals = [vals[(i - 1) % 4] for i in range(4)]
	else:
		new_vals = [vals[(i + 1) % 4] for i in range(4)]

	# 4개 strip 쓰기
	for i, (f, edge, rev) in enumerate(strips_info):
		v = new_vals[i]
		if rev:
			v = v[::-1]
		set_strip(cube, f, edge, v)

def parse_input():
    input = sys.stdin.readline

    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        n = int(input().strip())
        ops = input().split()

        test_cases.append((n, ops))

    return T, test_cases


if __name__ == "__main__":
	cubing()
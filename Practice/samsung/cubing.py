import sys

def cubing():
    T, test_cases = parse_input()

    for n, ops in test_cases:
        solve_cubing(n, ops)

def solve_cubing(n ,ops):
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

def rotate_face(cube, op):
	face = cube[op[0]]
	dir = op[1]

	if dir == '+':
		face = [
			[ face[2][0], face[1][0], face[0][0] ],
			[ face[2][1], face[1][1], face[0][1] ],
            [ face[2][2], face[1][2], face[0][2] ],
		]
		# temp = [
		# 	face[0][0],
		# 	face[1][0],
		# 	face[2][0]
		# ]

		# face[0][0] = face[2][0]
		# face[1][0] = face[2][1]
		# face[2][0] = face[2][2]
		
		# face[2][0] = face[0][2]
		# face[2][1] = face[1][2]
		# face[2][2] = face[2][2]
		
		# face[0][2] = face[0][0]
		# face[1][2] = face[0][1]
		# face[2][2] = face[0][2]

		# face[0][0] = temp[0]
		# face[0][1] = temp[1]
		# face[0][2] = temp[2]

	elif dir == '-':
		face = [
            [face[0][2], face[1][2], face[2][2]],
            [face[0][1], face[1][1], face[2][1]],
            [face[0][0], face[1][0], face[2][0]],
        ]
		# temp = [
		# 	face[0][2],
		# 	face[1][2],
		# 	face[2][2],
		# ]
		
		# face[0][2] = face[2][0]
		# face[1][2] = face[2][1]
		# face[2][2] = face[2][2]
		
		# face[2][0] = face[0][0]
		# face[2][1] = face[1][0]
		# face[2][2] = face[2][0]
		
		# face[0][0] = face[0][0]
		# face[1][0] = face[0][1]
		# face[2][0] = face[0][2]

		# face[0][0] = temp[0]
		# face[0][1] = temp[1]
		# face[0][2] = temp[2]

def rotate(cube, op):
	rotate_face(cube, op)
	
	if op[0] == 'L':
		if op[1] == '+':
			to_move = ['U', 'F', 'D', 'B']
		elif op[1] == '-':
			to_move = ['U', 'B', 'D', 'F']

		temp = []
		for i in range(3):
			temp.append(cube[to_move[-1]][i][0])

		for t in range(len(to_move)-1, 0, -1):
			for i in range(3):
				cube[to_move[t]][i][0] = cube[to_move[t-1]][i][0]
		
		for i in range(3):
			cube[to_move[0]][i][0] = temp[i]

	elif op[0] == 'R':
		if op[1] == '+':
			to_move = ['U', 'B', 'D', 'F']
		elif op[1] == '-':
			to_move = ['U', 'F', 'D', 'B']

		temp = []
		for i in range(3):
			temp.append(cube[to_move[-1]][i][2])

		for t in range(len(to_move)-1, 0, -1):
			for i in range(3):
				cube[to_move[t]][i][2] = cube[to_move[t-1]][i][2]
		
		for i in range(3):
			cube[to_move[0]][i][2] = temp[i]

	elif op[0] == 'U':
		if op[1] == '+':
			to_move = ['B', 'R', 'F', 'L']
		elif op[1] =='-':
			to_move = ['B', 'L', 'F', 'R']
		
		temp = []
		for j in range(3):
			temp.append(cube[to_move[-1]][0][j])

		for t in range(len(to_move)-1, 0, -1):
			for j in range(3):
				cube[to_move[t]][0][j] = cube[to_move[t-1]][0][j]
		
		for j in range(3):
			cube[to_move[0]][0][j] = temp[j]

	elif op[0] == 'D':
		if op[1] == '+':
			to_move = ['B', 'L', 'F', 'R']
		elif op[1] == '-':
			to_move = ['B', 'R', 'F', 'L']
		
		temp = []
		for j in range(3):
			temp.append(cube[to_move[-1]][2][j])

		for t in range(len(to_move)-1, 0, -1):
			for j in range(3):
				cube[to_move[t]][2][j] = cube[to_move[t-1]][2][j]
		
		for j in range(3):
			cube[to_move[0]][2][j] = temp[j]

	elif op[0] == 'F':
		if op[1] == '+':
			to_move = ['U', 'R', 'D', 'L']

			temp = [
				cube['L'][0][2],
				cube['L'][1][2],
				cube['L'][2][2]
			]
			
			cube['L'][0][2] = cube['D'][0][0]
			cube['L'][1][2] = cube['D'][0][1]
			cube['L'][2][2] = cube['D'][0][2]
			
			cube['D'][0][0] = cube['R'][0][0]
			cube['D'][0][1] = cube['R'][1][0]
			cube['D'][0][2] = cube['R'][2][0]
			
			cube['R'][0][0] = cube['U'][2][0]
			cube['R'][1][0] = cube['U'][2][1]
			cube['R'][2][0] = cube['U'][2][2]

			cube['U'][2][0] = temp[0]
			cube['U'][2][1] = temp[1]
			cube['U'][2][2] = temp[2]

		elif op[1] == '-':
			to_move = ['U', 'L', 'D', 'R']

			temp = [
				cube['R'][0][0],
				cube['R'][1][0],
				cube['R'][2][0]
			]

			cube['R'][0][0] = cube['D'][0][0]
			cube['R'][1][0] = cube['D'][0][1]
			cube['R'][2][0] = cube['D'][0][2]

			cube['D'][0][0] = cube['L'][0][2]
			cube['D'][0][1] = cube['L'][1][2]
			cube['D'][0][2] = cube['L'][2][2]

			cube['L'][0][2] = cube['U'][2][0]
			cube['L'][1][2] = cube['U'][2][1]
			cube['L'][2][2] = cube['U'][2][2]

			cube['U'][2][0] = temp[0]
			cube['U'][2][1] = temp[1]
			cube['U'][2][2] = temp[2]
			

	elif op[0] == 'B':
		if op[1] == '+':
			to_move = ['U', 'L', 'D', 'R']
			
			temp = [
				cube['R'][0][2],
				cube['R'][1][2],
				cube['R'][2][2]
			]

			cube['R'][0][2] = cube['D'][0][0]
			cube['R'][1][2] = cube['D'][0][1]
			cube['R'][2][2] = cube['D'][0][2]

			cube['D'][0][0] = cube['L'][0][0]
			cube['D'][0][1] = cube['L'][1][0]
			cube['D'][0][2] = cube['L'][2][0]

			cube['L'][0][0] = cube['U'][0][0]
			cube['L'][1][0] = cube['U'][0][1]
			cube['L'][2][0] = cube['U'][0][2]

			cube['U'][0][0] = temp[0]
			cube['U'][0][1] = temp[1]
			cube['U'][0][2] = temp[2]

		elif op[1] == '-':
			to_move = ['U', 'R', 'D', 'L']		

			temp = [
				cube['L'][0][0],
				cube['L'][1][0],
				cube['L'][2][0]
			]
			
			cube['L'][0][0] = cube['D'][0][0]
			cube['L'][1][0] = cube['D'][0][1]
			cube['L'][2][0] = cube['D'][0][2]
			
			cube['D'][0][0] = cube['R'][0][2]
			cube['D'][0][1] = cube['R'][1][2]
			cube['D'][0][2] = cube['R'][2][2]
			
			cube['R'][0][2] = cube['U'][0][0]
			cube['R'][1][2] = cube['U'][0][1]
			cube['R'][2][2] = cube['U'][0][2]

			cube['U'][0][0] = temp[0]
			cube['U'][0][1] = temp[1]
			cube['U'][0][2] = temp[2]

def parse_input():
    input = sys.stdin.readline

    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        n = int(input().strip())
        ops = input().split()  # e.g. ["U+", "R-", "F+", ...]

        test_cases.append((n, ops))

    return T, test_cases


# example usage
if __name__ == "__main__":
	cubing()
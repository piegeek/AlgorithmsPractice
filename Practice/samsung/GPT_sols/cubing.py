import sys

# Still wrong...
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
    f = cube[op[0]]

    if op[1] == '+':
        cube[op[0]] = [
            [f[2][0], f[1][0], f[0][0]],
            [f[2][1], f[1][1], f[0][1]],
            [f[2][2], f[1][2], f[0][2]],
        ]
    else:
        cube[op[0]] = [
            [f[0][2], f[1][2], f[2][2]],
            [f[0][1], f[1][1], f[2][1]],
            [f[0][0], f[1][0], f[2][0]],
        ]

def rotate(cube, op):
    # 1️⃣ rotate edges FIRST

    if op[0] == 'F':
        if op[1] == '+':
            temp = cube['U'][2][:]

            for i in range(3):
                cube['U'][2][i] = cube['L'][2-i][2]
                cube['L'][2-i][2] = cube['D'][0][i]
                cube['D'][0][i] = cube['R'][i][0]
                cube['R'][i][0] = temp[i]

        else:  # F-
            temp = cube['U'][2][:]

            for i in range(3):
                cube['U'][2][i] = cube['R'][i][0]
                cube['R'][i][0] = cube['D'][0][i]
                cube['D'][0][i] = cube['L'][2-i][2]
                cube['L'][2-i][2] = temp[i]

    elif op[0] == 'B':
        if op[1] == '+':
            temp = cube['U'][0][:]

            for i in range(3):
                cube['U'][0][i] = cube['R'][i][2]
                cube['R'][i][2] = cube['D'][2][i]
                cube['D'][2][i] = cube['L'][2-i][0]
                cube['L'][2-i][0] = temp[i]

        else:  # B-
            temp = cube['U'][0][:]

            for i in range(3):
                cube['U'][0][i] = cube['L'][2-i][0]
                cube['L'][2-i][0] = cube['D'][2][i]
                cube['D'][2][i] = cube['R'][i][2]
                cube['R'][i][2] = temp[i]

    # other faces unchanged
    # else:
        # your original L R U D logic here (unchanged)
    elif op[0] == 'L':
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

    # 2️⃣ rotate the face LAST
    rotate_face(cube, op)

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
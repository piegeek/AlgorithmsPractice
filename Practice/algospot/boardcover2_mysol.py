import sys

def boardcover2():
    T, test_cases = parse_input()

    for H, W, R, C, board, block in test_cases:
        solve_boardcover2(H, W, R, C, board, block)

def solve_boardcover2(H, W, R, C, board, block):
	# Precomputation first
	board_state = 0
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				board_state += cell(i, j, W)

	shapes = create_shapes(R, C, block)

	moves = []

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				y, x = i, j
				for shape in shapes:
					shape_addable = True 
					for coord in shape:
						dy, dx = coord[0], coord[1]

						if not (0 <= y + dy and y + dy <= (H - 1) and 0 <= x + dx and x + dx <= (W - 1) and board[y+dy][x+dx] == 0):
							shape_addable = False

					if shape_addable == True:
						move = 0
						for coord in shape:
							dy, dx = coord[0], coord[1]
							move += cell(y+dy, x+dx, W)

						moves.append(move)

	cache = {}

	ret = 1 + solve(board_state, moves, cache)

	print(ret)
	return ret

def cell(y, x, W):
	return (1 << (W * y + x))

def solve(board, moves, cache):
	if board in cache: return cache[board]

	ret = 0
	# Not deciding wheter board is used or not; board is always used thus use for loops
	for move in moves:
		# print(board)
		if (board & move) == 0:
			ret = max(ret, solve(board | move, moves, cache) + 1)

	cache[board] = ret
	return ret

def create_shapes(R, C, block):
	shapes = []

	# Original
	start_y, start_x = get_start(R, C, block)
	original = []
	for i in range(R):
		for j in range(C):
			if block[i][j] == 1:
				original.append([i - start_y, j - start_x])

	# Rotate 90 degs
	rot90 = [[-1 for row in range(R)] for col in range(C)]
	for i in range(R):
		for j in range(C):
			rot90[j][i] = block[i][j]

	start_y, start_x = get_start(C, R, rot90)

	rot90_shapes = []
	for i in range(C):
		for j in range(R):
			if rot90[i][j] == 1:
				rot90_shapes.append([i - start_y, j - start_x])

	# Rotate 180 degs
	rot180 = [[-1 for col in range(C)] for row in range(R)]
	for i in range(C):
		for j in range(R):
			rot180[j][i] = rot90[i][j]

	start_y, start_x = get_start(R, C, rot180)

	rot180_shapes = []
	for i in range(R):
		for j in range(C):
			if rot180[i][j] == 1:
				rot180_shapes.append([i - start_y, j - start_x])

	# Rotate 270 degs
	rot270 = [[-1 for row in range(R)] for col in range(C)]
	for i in range(R):
		for j in range(C):
			rot270[j][i] = rot180[i][j]

	start_y, start_x = get_start(C, R, rot270)

	rot270_shapes = []
	for i in range(C):
		for j in range(R):
			if rot270[i][j] == 1:
				rot270_shapes.append([i - start_y, j - start_x])


	shapes.append(original)
	shapes.append(rot90_shapes)
	shapes.append(rot180_shapes)
	shapes.append(rot270_shapes)
	
	return shapes

def get_start(R, C, block):
	for i in range(R):
		for j in range(C):
			if block[i][j] == 1:
				return [i, j]

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # Board size H x W, Block size R x C
        H, W, R, C = map(int, input().split())

        # Game board
        board = [list(input().strip()) for _ in range(H)]
        assert all(len(row) == W for row in board)

        new_board = []

        for i in range(H):
        	new_row = []
        	for j in range(W):
        		if board[i][j] == '#':
        			new_row.append(1)
        		else:
        			new_row.append(0)

        	new_board.append(new_row)

        # Block shape
        block = [list(input().strip()) for _ in range(R)]
        assert all(len(row) == C for row in block)

        new_block = []
		
        for i in range(R):
        	new_row = []
        	for j in range(C):
        		if block[i][j] == '#':
        			new_row.append(1)
        		else:
        			new_row.append(0)

        	new_block.append(new_row)


        test_cases.append((H, W, R, C, new_board, new_block))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	boardcover2()
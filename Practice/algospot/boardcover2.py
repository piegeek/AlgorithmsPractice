import sys

def boardcover2():
    T, test_cases = parse_input()

    for H, W, R, C, board, block in test_cases:
        solve_boardcover2(H, W, R, C, board, block)

def solve_boardcover2(H, W, R, C, board, block):
	# # print(board)
	# # print(block)

	# shapes = create_shapes(R, C, block)

	# # print(shapes)

	# board_state = get_board_state(board)
	# cache = {}

	# ret = max_blocks(board, board_state, shapes, cache)

	# print(ret)

	# return ret

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

	# Add 1 since original board is also valid state
	ret = 1 + solve(board_state, moves, cache)

	print(ret)
	return ret

def cell(y, x, W):
	return (1 << (W * y + x))

def solve(board, moves, cache):
	if board in cache: return cache[board]

	# Why this has to be 1; 1 means there is always at least one move viable; what if no moves can be made? -> Fixed; must be 0
	ret = 0
	# Not deciding wheter board is used or not; board is always used thus use for loops
	for move in moves:
		# print(board)
		if (board & move) == 0:
			ret = max(ret, solve(board | move, moves, cache) + 1)

	cache[board] = ret
	return ret

def max_blocks(board, board_state, shapes, cache):
	# print(board_state)
	if board_state in cache: return cache[board_state]

	# variable max_count is used only when another shape can be placed; thus it should start from 1
	max_count = 1

	can_place_more = False

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				for shape in shapes:
					can_place_shape = True
					for coord in shape:
						dy, dx = coord[0], coord[1]

						if not ((0 <= i + dy and i + dy <= len(board) - 1) and (0 <= j + dx and j + dx <= len(board[0]) - 1) and board[i+dy][j+dx] == 0):
							can_place_shape = False

					if can_place_shape:
						can_place_more = True

						for coord in shape:
							dy, dx = coord[0], coord[1]

							board[i+dy][j+dx] = 1

						new_board_state = get_board_state(board)

						max_count = max(max_count, max_blocks(board, new_board_state, shapes, cache))

						# Backtracking
						for coord in shape:
							dy, dx = coord[0], coord[1]

							board[i+dy][j+dx] = 0

	if can_place_more:
		cache[board_state] = 1 + max_count
		return 1 + max_count
	else:
		cache[board_state] = 0
		return 0

def get_board_state(board):
	state = 0

	count = 0

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				state |= (1 << count)

			count += 1

	return state

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

	# Flipped
	flipped_block = block[::-1]
	start_y, start_x = get_start(R, C, flipped_block)
	flipped = []
	for i in range(R):
		for j in range(C):
			if flipped_block[i][j] == 1:
				flipped.append([i - start_y, j - start_x])

	# Rotate 90 degs
	flip_rot90 = [[-1 for row in range(R)] for col in range(C)]
	for i in range(R):
		for j in range(C):
			flip_rot90[j][i] = flipped_block[i][j]

	start_y, start_x = get_start(C, R, flip_rot90)

	flip_rot90_shapes = []
	for i in range(C):
		for j in range(R):
			if flip_rot90[i][j] == 1:
				flip_rot90_shapes.append([i - start_y, j - start_x])

	# Rotate 180 degs
	flip_rot180 = [[-1 for col in range(C)] for row in range(R)]
	for i in range(C):
		for j in range(R):
			flip_rot180[j][i] = flip_rot90[i][j]

	start_y, start_x = get_start(R, C, flip_rot180)

	flip_rot180_shapes = []
	for i in range(R):
		for j in range(C):
			if flip_rot180[i][j] == 1:
				flip_rot180_shapes.append([i - start_y, j - start_x])

	# Rotate 270 degs
	flip_rot270 = [[-1 for row in range(R)] for col in range(C)]
	for i in range(R):
		for j in range(C):
			flip_rot270[j][i] = flip_rot180[i][j]

	start_y, start_x = get_start(C, R, flip_rot270)

	flip_rot270_shapes = []
	for i in range(C):
		for j in range(R):
			if flip_rot270[i][j] == 1:
				flip_rot270_shapes.append([i - start_y, j - start_x])

	shapes.append(original)
	shapes.append(rot90_shapes)
	shapes.append(rot180_shapes)
	shapes.append(rot270_shapes)
	# shapes.append(flipped)
	# shapes.append(flip_rot90_shapes)
	# shapes.append(flip_rot180_shapes)
	# shapes.append(flip_rot270_shapes)
	
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

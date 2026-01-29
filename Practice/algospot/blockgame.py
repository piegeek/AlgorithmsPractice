import sys

def blockgame():
    C, test_cases = parse_input()

    for board in test_cases:
        solve_blockgame(board)

def solve_blockgame(board):
	# Still takes too long even with memoization...
	shapes = [
		[[0, 0], [0, 1]],
		[[0, 0], [1, 0]],
		[[0, 0], [1, 0], [1, 1]],
		[[0, 0], [1, 0], [1, -1]],
		[[0, 0], [1, 0], [0, 1]],
		[[0, 0], [0, 1], [1, 1]]
	]

	# return can_win(board, shapes)

	cache = {}

	board_state = 0
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				board_state += cell(i, j)

	ret = can_win(board, board_state, shapes, cache)
	# print(can_win_first_empty_only(board, shapes, cache))

	print(ret)
	return ret

	# Precalculation and caching; book's solution
	# moves = generate_moves()

	# board_state = 0
	# for i in range(len(board)):
	# 	for j in range(len(board[i])):
	# 		if board[i][j] == 1:
	# 			board_state += cell(i, j)

	# cache = {}
	# ret = solve(board_state, moves, cache)

	# print(ret)
	# return ret

def cell(y, x):
	return (1 << (5 * y + x))

# Solve with precomputation
def generate_moves():
	moves = []

	for i in range(4):
		for j in range(4):
			y, x = i, j
			shapes = []
			for dy in range(2):
				for dx in range(2):
					shapes.append(cell(y+dy, x+dx))

			square = sum(shapes)

			for shape in shapes:
				moves.append(square - shape)

	for i in range(4):
		for j in range(4):
			y, x, = i, j
			moves.append(cell(y, x) + cell(y, x+1))
			moves.append(cell(y, x) + cell(y+1, x))

	# Last row
	for j in range(4):
		y, x, = 4, j
		moves.append(cell(y, x) + cell(y, x+1))

	# Last column
	for i in range(4):
		y, x = i, 4
		moves.append(cell(y, x) + cell(y+1, x))

	return moves

def solve(board, moves, cache):
	if board in cache: return cache[board]

	for move in moves:
		if (board & move) == 0:
			if not solve((board | move), moves, cache):
				cache[board] = True
				return True
	
	cache[board] = False
	return False

# Requires memoization; solves the same board multiple times
def can_win(board, board_state, shapes, cache):
	if board_state in cache: return cache[board_state]

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				for shape in shapes:
					can_place_shape = True
					for coord in shape:
						dy, dx = coord[0], coord[1]

						if not (0 <= i + dy and i + dy <= 4 and 0 <= j + dx and j + dx <= 4 and board[i+dy][j+dx] == 0):
							# print('here')
							can_place_shape = False
							break

					if can_place_shape:
						shape_state = 0
						for coord in shape:
							dy, dx = coord[0], coord[1]

							board[i+dy][j+dx] = 1
							shape_state += cell(i+dy, j+dx)

						next_player_winnable = can_win(board, board_state | shape_state, shapes, cache)

						if next_player_winnable:
							# Backtracking
							for coord in shape:
								dy, dx = coord[0], coord[1]

								board[i+dy][j+dx] = 0

							continue
						# Winnable
						else:
							# Backtracking; mandatory backtracking
							for coord in shape:
								dy, dx = coord[0], coord[1]

								board[i+dy][j+dx] = 0

							cache[board_state] = True
							return True
	
	cache[board_state] = False
	return False

# Only checks first empty location; returns too early
# Now this gives False for the first input ???
def can_win_first_empty_only(board, shapes, cache):
	board_state = get_bin(board)
	if board_state in cache: return cache[board_state]

	first_empty_found = False

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				
				y, x = i, j
				first_empty_found = True
				break

		if first_empty_found:
			break

	if not first_empty_found: 
		cache[board_state] = False
		return False

	for shape in shapes:
		can_place_shape = True
		for coord in shape:
			dy, dx = coord[0], coord[1]

			if not (0 <= y + dy and y + dy <= 4 and 0 <= x + dx and x + dx <= 4 and board[y+dy][x+dx] == 0):
				# print('here')
				can_place_shape = False
				break

		if can_place_shape:
			for coord in shape:
				dy, dx = coord[0], coord[1]

				board[y+dy][x+dx] = 1

			next_player_winnable = can_win(board, shapes, cache)

			if next_player_winnable:
				# Backtracking
				for coord in shape:
					dy, dx = coord[0], coord[1]

					board[y+dy][x+dx] = 0

				continue
			# Winnable
			else:
				# Backtracking; mandatory backtracking
				for coord in shape:
					dy, dx = coord[0], coord[1]

					board[y+dy][x+dx] = 0

				cache[board_state] = True
				return True

	cache[board_state] = False
	return False
	

def get_bin(board):
	bin_list = []

	for i in range(len(board)):
		for j in range(len(board[i])):
			bin_list.append(str(board[i][j]))

	bin_str = ''.join(bin_list)

	return int(bin_str, base=2)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        board = []
        for _ in range(5):
            row = input().strip()

            conv_row = []

            for char in row:
                if char == '#':
                	conv_row.append(1)
                elif char == '.':
                	conv_row.append(0)

            board.append(conv_row)
        test_cases.append(board)

    return C, test_cases


# Example usage
if __name__ == "__main__":
	blockgame()

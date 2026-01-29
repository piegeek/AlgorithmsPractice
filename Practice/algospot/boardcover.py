def boardcover():
	test_cases = parse_input()

	for H, W, board in test_cases:
		count = [0]
		solve_boardcover(H, W, board, count)
		print(count[0])

def solve_boardcover(H, W, board, count):
	for i in range(H):
		for j in range(W):
			if board[i][j] == '.':
				available_blocks = get_available_blocks(board, i, j)

				# Leaf node
				if len(available_blocks) == 0:
					return False

				tried_all_yet_failed = True

				for block in available_blocks:
					for spot in block:
						r, c = spot[0], spot[1]
						board[r][c] = '#'
					
					if solve_boardcover(H, W, board, count) == True:
						# No! - Overcounting; incremented at each recursive return; should increment at the base case
						# count[0] += 1
						tried_all_yet_failed = False
					else:
						pass
						
					# Backtracking
					for spot in block:
						r, c = spot[0], spot[1]
						board[r][c] = '.'

				if tried_all_yet_failed:
					return False

	# Increment count at leaf node
	count[0] += 1
	return True
					

def get_available_blocks_2(board, i, j):
	blocks = []

	# Down, Right
	if i < len(board) - 1 and j < len(board[0]) - 1 and board[i+1][j] == '.' and board[i+1][j+1] == '.':
		blocks.append([
			[i, j],
			[i+1, j],
			[i+1, j+1]
		])
	# Up, Right
	if i > 0 and j < len(board[0]) - 1 and board[i-1][j] == '.' and board[i-1][j+1] == '.':
		blocks.append([
			[i, j],
			[i-1, j],
			[i-1, j+1]
		])
	# Down, Left
	if i < len(board) - 1 and j > 0 and board[i+1][j] == '.' and board[i+1][j-1] == '.':
		blocks.append([
			[i, j],
			[i+1, j],
			[i+1, j-1]
		])
	# Up, Left
	if i > 0 and j > 0 and board[i-1][j] == '.' and board[i-1][j-1] == '.':
		blocks.append([
			[i, j],
			[i-1, j],
			[i-1, j-1]
		])

	# [i, j] is not in the middle
	# North
	if i < len(board) - 1 and j < len(board[0]) - 1 and board[i+1][j] == '.' and board[i+1][j+1] == '.':
		blocks.append([
			[i, j],
			[i+1, j],
			[i+1, j+1]
		])

	if i < len(board) - 1 and j > 0 and board[i+1][j] == '.' and board[i+1][j-1] == '.':
		blocks.append([
			[i, j],
			[i+1, j],
			[i+1, j-1]
		])

	# East
	if i > 0 and j > 0 and board[i][j-1] == '.' and board[i-1][j-1] == '.':
		blocks.append([
			[i, j],
			[i, j-1],
			[i-1, j-1]
		])

	if i < len(board) - 1 and j > 0 and board[i][j-1] == '.' and board[i+1][j-1] == '.':
		blocks.append([
			[i, j],
			[i, j-1],
			[i+1, j-1]
		])

	# South
	if i > 0 and j < len(board[0]) - 1 and board[i-1][j] == '.' and board[i-1][j+1] == '.':
		blocks.append([
			[i, j],
			[i-1, j],
			[i-1, j+1]
		])

	if i > 0 and j > 0 and board[i-1][j] == '.' and board[i-1][j-1] == '.':
		blocks.append([
			[i, j],
			[i-1, j],
			[i-1, j-1]
		])

	# West
	if i > 0 and j < len(board[0]) - 1 and board[i][j+1] == '.' and board[i-1][j+1] == '.':
		blocks.append([
			[i, j],
			[i, j+1],
			[i-1, j+1]
		])

	if i < len(board) - 1 and j < len(board[0]) - 1 and board[i][j+1] == '.' and board[i+1][j+1] == '.':
		blocks.append([
			[i, j],
			[i, j+1],
			[i+1, j+1]
		])


	return blocks

'''
Possible candidates
A:   B:   C:   D:
##   ##   #    #
#     #   ##  ##
'''

def get_available_blocks(board, i, j):
    blocks = []
    H = len(board)
    W = len(board[0])

    # 4 possible L-shaped blocks
    shapes = [
        [(0, 0), (1, 0), (0, 1)],
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 0), (1, 0), (1, -1)],
    ]

    for shape in shapes:
        coords = []
        valid = True
        for dr, dc in shape:
            r = i + dr
            c = j + dc
            if r < 0 or r >= H or c < 0 or c >= W or board[r][c] != '.':
                valid = False
                break
            coords.append((r, c))
        if valid:
            blocks.append(coords)

    return blocks

def parse_input():
    C = int(input().strip())  # number of test cases
    test_cases = []

    for _ in range(C):
        H, W = map(int, input().split())

        board = []
        for _ in range(H):
            row = list(input().strip())
            board.append(row)

        test_cases.append((H, W, board))

    return test_cases

if __name__ == '__main__':
	boardcover()
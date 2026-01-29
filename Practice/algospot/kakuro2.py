import sys

def kakuro2():
    T, test_cases = parse_input()

    for N, board, Q, hints in test_cases:
        placed = [[False for _ in range(N)] for _ in range(N)]
        solve_kakuro2(N, board, Q, hints, placed)
        print(board)

def solve_kakuro2(N, board, Q, hints, placed):
    if check_valid_kakuro(board, hints, placed):
        return True

    # print(board[-1])
    for i in range(N):
    	for j in range(N):
    		if board[i][j] == 1 and placed[i][j] == False:
    			can_place = False
    			for x in range(1, 9+1):
    				if check_valid(i, j, board, x, placed):
    					can_place = True
    					board[i][j] = x
    					placed[i][j] = True
    					
    					can_solve = solve_kakuro2(N, board, Q, hints, placed)

    					if can_solve:
    						return True
    					else:
    						# Backtrack
    						board[i][j] = 1
    						placed[i][j] = False
    						can_place = False

    			if can_place == False:
    				return False

    return False


def check_valid_kakuro(board, hints, placed):
	for hint in hints:
		y, x, direction, total = hint
		# (y, x) is the 1-based coordinate
		y -= 1
		x -= 1
		# Horizontal sum
		if direction == 0:
			r, c = y, x + 1
			hor_sum = 0
			hor_items = []
			while board[r][c] != 0:
				if placed[r][c] == False:
					return False
				if board[r][c] not in hor_items:
					hor_items.append(board[r][c])
				else:
					return False
				hor_sum += board[r][c]

				c += 1

			if hor_sum != total:
				return False

		# Vertical sum
		elif direction == 1:
			r, c = y + 1, x
			ver_sum = 0
			ver_items = []
			while board[r][c] != 0:
				if placed[r][c] == False:
					return False
				if board[r][c] not in ver_items:
					ver_items.append(board[r][c])
				else:
					return False
				ver_sum += board[r][c]

				r += 1

		if ver_sum != total:
			return False

	return True


def check_valid(i, j, board, x, placed):
	last_zero_idx_j = j - 1 - board[i][:j][::-1].index(0)
	last_zero_idx_i = i - 1 - [ board[r][j] for r in range(i - 1, -1, -1) ].index(0)

	r = last_zero_idx_i + 1
	while r <= len(board) - 1 and board[r][j] != 0:
		if placed[r][j] == True and board[r][j] == x:
			return False

		r += 1

	c = last_zero_idx_j + 1
	while c <= len(board[i]) - 1 and board[i][c] != 0:
		if placed[i][c] == True and board[i][c] == x:
			return False

		c += 1

	return True


def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # Size of the board
        N = int(input().strip())

        # Board description (0 = black/hint, 1 = white)
        board = [list(map(int, input().split())) for _ in range(N)]
        assert all(len(row) == N for row in board)

        # Number of hints
        Q = int(input().strip())

        hints = []
        for _ in range(Q):
            y, x, direction, total = map(int, input().split())
            hints.append((y, x, direction, total))

        test_cases.append((N, board, Q, hints))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	kakuro2()
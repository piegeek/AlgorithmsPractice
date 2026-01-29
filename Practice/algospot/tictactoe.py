import sys

def tictactoe():
    C, test_cases = parse_input()
    for board in test_cases:
        solve_tictactoe(board)

def solve_tictactoe(board):
	# Count o
	two_count = 0
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 2:
				two_count += 1

	# X starts
	if two_count % 2 == 0:
		winner = dfs(board, 0)
	# O starts
	else:
		winner = dfs(board, 1)

	if winner == 1:
		print('x')
	elif winner == 2:
		print('o')
	elif winner == -1:
		print('TIE')


def dfs(board, count):
	if count % 2 == 0:
		player = 1 
		other_player = 2
	else:
		player = 2
		other_player = 1

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 0:
				board[i][j] = player

				if check_win(board, player): 
					# Backtracking !!! IMPORTANT
					board[i][j] = 0
					return player

				winner = dfs(board, count+1)

				if winner == player:
					# Backtracking
					board[i][j] = 0
					return player
				elif winner == other_player:
					# Backtracking
					board[i][j] = 0
					continue
				elif winner == -1:
					# Backtracking
					board[i][j] = 0
					return -1

	# Leaf node; base case
	if check_win(board, player): return player
	else: 
		# Tie
		if check_win(board, other_player) == False:
			return -1
		else:
			return other_player

def check_win(board, player):
	for i in range(len(board)):
		if board[i][0] == player and board[i][1] == player and board[i][2] == player:
			return True

	for j in range(len(board[0])):
		if board[0][j] == player and board[1][j] == player and board[2][j] == player:
			return True

	diagonal_equal = True
	
	for x in range(3):
		if board[x][x] != player:
			diagonal_equal = False

	if diagonal_equal: return True

	diagonal_inv_equal = True
	
	for x in range(3):
		if board[x][2-x] != player:
			diagonal_inv_equal = False

	if diagonal_inv_equal: return True

	return False

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        board = []
        for _ in range(3):
            row = input().strip()   # exactly 3 characters

            converted_row = []

            for item in row:
            	if item == 'x':
            		converted_row.append(1)
            	elif item == 'o':
            		converted_row.append(2)
            	elif item == '.':
            		converted_row.append(0)

            board.append(converted_row)
        test_cases.append(board)

    return C, test_cases


# Example usage
if __name__ == "__main__":
	tictactoe()

import sys
import copy

def twentyfourtyeight():
    N, board = parse_input()
    solve_twentyfourtyeight(N, board)

def solve_twentyfourtyeight(N, board):
	moves = {
		'UP': [-1, 0],
		'RIGHT': [0, 1],
		'DOWN': [1, 0],
		'LEFT': [0, -1]
	}

	combined = [ [ False for _ in range(N) ] for _ in range(N) ]

	ret = dfs(N, board, 0, moves, combined)

	print(ret)
	return ret

def dfs(N, board, count, moves, combined):
	# Leaf node
	if count == 5:
		max_block_val = 0
		for i in range(N):
			for j in range(N):
				max_block_val = max(max_block_val, board[i][j])

		return max_block_val

	ret = 0

	for move in moves:
		dy, dx = moves[move][0], moves[move][1]
		board_copy = copy.deepcopy(board)
		merge(board, dy, dx, combined, move)
		ret = max(
			ret,
			dfs(N, board, count+1, moves, combined)
		)
		# Backtracking
		board = board_copy
		combined = [ [ False for _ in range(N) ] for _ in range(N) ]

	return ret

def merge(board, dy, dx, combined, move):
	if move == 'UP' or move == 'LEFT':
		for i in range(len(board)):
			for j in range(len(board[i])):
				r, c = i, j
				while True:
					if 0 <= r + dy and r + dy <= len(board) - 1 and 0 <= c + dx and c + dx <= len(board[0]) - 1:
						if board[r+dy][c+dx] == 0:
							board[r+dy][c+dx] = board[r][c]
							board[r][c] = 0

							r += dy
							c += dx

						elif board[r+dy][c+dx] > 0 and board[r+dy][c+dx] == board[r][c] and combined[r+dy][c+dx] == False:
							board[r+dy][c+dx] *= 2
							combined[r+dy][c+dx] = True
							board[r][c] = 0

							r += dy
							c += dx

						elif board[r+dy][c+dx] > 0 and board[r+dy][c+dx] == board[r][c] and combined[r+dy][c+dx] == True:
							break
						else:
							break
					else: 
						break
	else:
		for i in range(len(board)-1, -1, -1):
			for j in range(len(board[i])-1, -1, -1):
				r, c = i, j
				while True:
					if 0 <= r + dy and r + dy <= len(board) - 1 and 0 <= c + dx and c + dx <= len(board[0]) - 1:
						if board[r+dy][c+dx] == 0:
							board[r+dy][c+dx] = board[r][c]
							board[r][c] = 0

							r += dy
							c += dx

						elif board[r+dy][c+dx] > 0 and board[r+dy][c+dx] == board[r][c] and combined[r+dy][c+dx] == False:
							board[r+dy][c+dx] *= 2
							combined[r+dy][c+dx] = True
							board[r][c] = 0

							r += dy
							c += dx

						elif board[r+dy][c+dx] > 0 and board[r+dy][c+dx] == board[r][c] and combined[r+dy][c+dx] == True:
							break
						else:
							break
					else: 
						break


def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())
    board = []

    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)

    return N, board


# example usage
if __name__ == "__main__":
	twentyfourtyeight()
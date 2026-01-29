import sys

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

def dicerolling():
    N, M, x, y, K, board, commands = parse_input()
    solve_dicerolling(N, M, x, y, K, board, commands)

def solve_dicerolling(N, M, x, y, K, board, commands):
	dice = {
		'top': 0,
		'left': 0,
		'right': 0,
		'front': 0,
		'back': 0,
		'bottom': 0
	}

	r, c = y, x

	for i in range(len(commands)):
		# DOWN
		if commands[i] == 4:
			dy, dx = 1, 0
			if 0 <= r + dy and r + dy <= N - 1 and 0 <= c + dx and c + dx <= M - 1:
				r += dy
				c += dx

				move(dice, DOWN)
				
				if board[r][c] == 0:
					board[r][c] = dice['bottom']
				else:
					dice['bottom'] = board[r][c]
					board[r][c] = 0

				print(dice['top'])
		# RIGHT
		elif commands[i] == 1:
			dy, dx = 0, 1
			if 0 <= r + dy and r + dy <= N - 1 and 0 <= c + dx and c + dx <= M - 1:
				r += dy
				c += dx

				move(dice, RIGHT)
				
				if board[r][c] == 0:
					board[r][c] = dice['bottom']
				else:
					dice['bottom'] = board[r][c]
					board[r][c] = 0
				
				print(dice['top'])
		# UP
		elif commands[i] == 3:
			dy, dx = -1, 0
			if 0 <= r + dy and r + dy <= N - 1 and 0 <= c + dx and c + dx <= M - 1:
				r += dy
				c += dx

				move(dice, UP)
				
				if board[r][c] == 0:
					board[r][c] = dice['bottom']
				else:
					dice['bottom'] = board[r][c]
					board[r][c] = 0
				
				print(dice['top'])
		# LEFT
		elif commands[i] == 2:
			dy, dx = 0, -1
			if 0 <= r + dy and r + dy <= N - 1 and 0 <= c + dx and c + dx <= M - 1:
				r += dy
				c += dx

				move(dice, LEFT)
				
				if board[r][c] == 0:
					board[r][c] = dice['bottom']
				else:
					dice['bottom'] = board[r][c]
					board[r][c] = 0
				
				print(dice['top'])

def move(dice, direction):
	if direction == DOWN:
		temp = dice['top']
		dice['top'] = dice['back']
		dice['back'] = dice['bottom']
		dice['bottom'] = dice['front']
		dice['front'] = temp

	elif direction == RIGHT:
		temp = dice['top']
		dice['top'] = dice['left']
		dice['left'] = dice['bottom']
		dice['bottom'] = dice['right']
		dice['right'] = temp

	elif direction == UP:
		temp = dice['top']
		dice['top'] = dice['front']
		dice['front'] = dice['bottom']
		dice['bottom'] = dice['back']
		dice['back'] = temp

	elif direction == LEFT:
		temp = dice['top']
		dice['top'] = dice['right']
		dice['right'] = dice['bottom']
		dice['bottom'] = dice['left']
		dice['left'] = temp


def parse_input():
    input = sys.stdin.readline

    N, M, x, y, K = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    commands = list(map(int, input().split()))

    return N, M, x, y, K, board, commands


# example usage
if __name__ == "__main__":
	dicerolling()
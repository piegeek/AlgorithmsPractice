import sys
import heapq

EMPTY = 0
WALL = 1
RED = 7
BLUE = 8
HOLE = 9

def marbleescape():
    N, M, board, red, blue, hole = parse_input()
    solve_marbleescape(N, M, board, red, blue, hole)

def solve_marbleescape(N, M, board, red, blue, hole):
	moves = {
		'RIGHT': [0, 1],
		'DOWN' : [1, 0],
		'LEFT' : [0, -1],
		'UP'   : [-1, 0]
	}

	queue = []

	heapq.heappush(queue, [0, red, blue])

	move_count = 0

	while len(queue) > 0 and move_count < 10 + 1:
		move_count, red_val, blue_val = heapq.heappop(queue)

		# Blue falls into hole -> Fail
		if blue_val == hole:
			continue

		if red_val == hole:
			print(move_count)
			return move_count

		board[red[0]][red[1]] = EMPTY
		board[red_val[0]][red_val[1]] = RED
		
		board[blue[0]][blue[1]] = EMPTY
		board[blue_val[0]][blue_val[1]] = BLUE

		# Move right
		new_red, new_blue = move_marble(red_val, blue_val, hole, N, M, moves, 'RIGHT', board)
		heapq.heappush(queue, [move_count+1, new_red, new_blue])

		# Move down
		new_red, new_blue = move_marble(red_val, blue_val, hole, N, M, moves, 'DOWN', board)
		heapq.heappush(queue, [move_count+1, new_red, new_blue])
		
		# Move left
		new_red, new_blue = move_marble(red_val, blue_val, hole, N, M, moves, 'LEFT', board)
		heapq.heappush(queue, [move_count+1, new_red, new_blue])
		
		# Move up
		new_red, new_blue = move_marble(red_val, blue_val, hole, N, M, moves, 'UP', board)
		heapq.heappush(queue, [move_count+1, new_red, new_blue])

		# Backtracking
		board[red[0]][red[1]] = RED
		board[red_val[0]][red_val[1]] = EMPTY
		
		board[blue[0]][blue[1]] = BLUE
		board[blue_val[0]][blue_val[1]] = EMPTY

	print(-1)
	return -1

def move_marble(red, blue, hole, N, M, moves, direction, board):
	red_r, red_c = red[0], red[1]
	blue_r, blue_c = blue[0], blue[1]

	dy, dx = moves[direction][0], moves[direction][1]

	red_first = True
	if direction == 'RIGHT':
		if red_c > blue_c:
			red_first = True
		else:
			red_first = False

	elif direction == 'DOWN':
		if red_r > blue_r:
			red_first = True
		else:
			red_first = False

	elif direction == 'LEFT':
		if red_c < blue_c:
			red_first = True
		else:
			red_first = False

	elif direction == 'UP':
		if red_r > blue_r:
			red_first = True
		else:
			red_first = False

	if red_first:
		while True:
			if 0 <= red_r + dy and red_r + dy <= N-1 and 0 <= red_c + dx and red_c + dx <= M-1 and board[red_r+dy][red_c+dx] == EMPTY:
				board[red_r][red_c] = EMPTY
				red_r += dy
				red_c += dx
				board[red_r][red_c] = RED
			else:
				red_cant_move = True
				break

		if board[red_r+dy][red_c+dx] == HOLE:
			board[red_r][red_c] = EMPTY
			red_r += dy
			red_c += dx
			board[red_r][red_c] = HOLE

		while True:
			if 0 <= blue_r + dy and blue_r + dy <= N-1 and 0 <= blue_c + dx and blue_c + dx <= M-1 and board[blue_r+dy][blue_c+dx] == EMPTY:
				board[blue_r][blue_c] = EMPTY
				blue_r += dy
				blue_c += dx
				board[blue_r][blue_c] = BLUE
			else:
				blue_cant_move = True
				break

		if board[blue_r+dy][blue_c+dx] == HOLE:
			board[blue_r][blue_c] = EMPTY
			blue_r += dy
			blue_c += dx
			board[blue_r][blue_c] = HOLE

	else:
		while True:
			if 0 <= blue_r + dy and blue_r + dy <= N-1 and 0 <= blue_c + dx and blue_c + dx <= M-1 and board[blue_r+dy][blue_c+dx] == EMPTY:
				board[blue_r][blue_c] = EMPTY
				blue_r += dy
				blue_c += dx
				board[blue_r][blue_c] = BLUE
			else:
				blue_cant_move = True
				break

		if board[blue_r+dy][blue_c+dx] == HOLE:
			board[blue_r][blue_c] = EMPTY
			blue_r += dy
			blue_c += dx
			board[blue_r][blue_c] = HOLE

		while True:
			if 0 <= red_r + dy and red_r + dy <= N-1 and 0 <= red_c + dx and red_c + dx <= M-1 and board[red_r+dy][red_c+dx] == EMPTY:
				board[red_r][red_c] = EMPTY
				red_r += dy
				red_c += dx
				board[red_r][red_c] = RED
			else:
				red_cant_move = True
				break

		if board[red_r+dy][red_c+dx] == HOLE:
			board[red_r][red_c] = EMPTY
			red_r += dy
			red_c += dx
			board[red_r][red_c] = HOLE

	# Backtracking
	board[red[0]][red[1]] = RED
	board[blue[0]][blue[1]] = BLUE
	board[hole[0]][hole[1]] = HOLE

	return [[red_r, red_c], [blue_r, blue_c]]
	

def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    board = []

    red = blue = hole = None

    for i in range(N):
        row = list(input().rstrip())

        new_row = []

        for char in row:
        	if char == '.':
        		new_row.append(EMPTY)
        	elif char == '#':
        		new_row.append(WALL)
        	elif char == 'R':
        		new_row.append(RED)
        	elif char == 'B':
        		new_row.append(BLUE)
        	elif char == 'O':
        		new_row.append(HOLE)

        board.append(new_row)

        for j, cell in enumerate(row):
            if cell == 'R':
                red = [i, j]
            elif cell == 'B':
                blue = [i, j]
            elif cell == 'O':
                hole = [i, j]

    return N, M, board, red, blue, hole


# example usage
if __name__ == "__main__":
	marbleescape()
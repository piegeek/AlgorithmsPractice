import sys
import copy

def snake():
    N, apples, turns = parse_input()
    solve_snake(N, apples, turns)

def solve_snake(N, apples, turns):
	moves = [
		[-1, 0], # UP
		[0, 1],  # RIGHT
		[1, 0],  # DOWN
		[0, -1]  # LEFT
	]

	apples_eaten = [ False for _ in range(len(apples)) ]
	turns_seconds = [ x[0] for x in turns ]

	# Starts moving in the right direction
	current_move = 1

	head_r, head_c = 0, 0
	second_count = 0

	snake = [[0, 0]]

	dy, dx = 0, 0

	while 0 <= head_r and head_r <= N-1 and 0 <= head_c and head_c <= N-1:
		if [head_r + dy, head_c + dx] in snake[:-1]:
			second_count += 1
			break

		# print(f'head_r: {head_r}, head_c: {head_c}')
		# print(f'second_count: {second_count}')

		# print(snake)

		if second_count in turns_seconds:
			turn_idx = turns_seconds.index(second_count)

			direction = turns[turn_idx][1]

			next_move = get_next_move(direction, moves, current_move)

			current_move = next_move

		dy, dx = moves[current_move][0], moves[current_move][1]
		
		if (head_r, head_c) in apples:
			apple_idx = apples.index((head_r, head_c))
			if apples_eaten[apple_idx] == False:
				head_r += dy
				head_c += dx
				apples_eaten[apple_idx] = True

				snake.append([head_r, head_c])
				
				second_count += 1

				continue

		for i in range(len(snake)-1):
			snake[i][0] = snake[i+1][0]
			snake[i][1] = snake[i+1][1]
		
		head_r += dy
		head_c += dx
		
		snake[-1][0] = head_r
		snake[-1][1] = head_c

		second_count += 1

	print(second_count)
	return second_count

def get_next_move(direction, moves, current_move):
	if direction == 'L':
		turn_signal = -1
	else:
		turn_signal = 1

	return (len(moves) + current_move + turn_signal) % len(moves)

def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())

    K = int(input().strip())
    apples = []
    for _ in range(K):
        r, c = map(int, input().split())
        apples.append((r - 1, c - 1))  # convert to 0-based

    L = int(input().strip())
    turns = []
    for _ in range(L):
        X, C = input().split()
        turns.append((int(X), C))

    return N, apples, turns


# example usage
if __name__ == "__main__":
	snake()
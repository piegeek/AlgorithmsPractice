import sys

def robotcleaner():
    N, M, r, c, d, room = parse_input()
    solve_robotcleaner(N, M, r, c, d, room)

def solve_robotcleaner(N, M, r, c, d, room):
	moves = [
		# RIGHT
		[0, 1],
		# DOWN
		[1, 0],
		# LEFT
		[-1, 0],
		# UP
		[-1, 0]
	]

	ret = dfs(N, M, r, c, d, room, moves)

	# print(room)

	print(ret)
	return ret

	# DFS NEW
	# count = [0]
	# dfs_new(N, M, r, c, room, moves, count)

	# ret = count[0]

	# print(ret)
	# return ret

def dfs(N, M, r, c, d, room, moves):
	ret = 1

	if room[r][c] == 0:
		room[r][c] = 2

	no_more_left_to_clean = True
	for move in moves:
		dy, dx = move
		if 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= M-1 and room[r+dy][c+dx] == 0 :
			no_more_left_to_clean = False
			while d_move(d) != move:
				d = rotate_90deg(d)

			ret += dfs(N, M, r+dy, c+dx, d, room, moves)

	if no_more_left_to_clean:
		dy, dx = (-1) * d_move(d)[0], (-1) * d_move(d)[1]
		if 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= M-1 and room[r+dy][c+dx] != 1:
			ret += dfs(N, M, r+dy, c+dx, d, room, moves)

	return ret

def dfs_new(N, M, r, c, room, moves, count):
	if room[r][c] == 0:
		count[0] += 1
		room[r][c] = 2

	elif room[r][c] == 2:
		count[0] += 1

	no_more_left_to_clean = True

	for move in moves:
		dy, dx = move
		if 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= M-1 and room[r+dy][c+dx] == 0:
			no_more_left_to_clean = False
			dfs_new(N, M, r+dy, c+dx, room, moves, count)


def rotate_90deg(d):
	if d == 0:
		return 3
	elif d == 1:
		return 0
	elif d == 2:
		return 1
	elif d == 3:
		return 2

def d_move(d):
	if d == 0:
		return [-1, 0]
	elif d == 1:
		return [0, 1]
	elif d == 2:
		return [1, 0]
	elif d == 3:
		return [-1, 0]

def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    r, c, d = map(int, input().split())

    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))

    return N, M, r, c, d, room


# example usage
if __name__ == "__main__":
	robotcleaner()
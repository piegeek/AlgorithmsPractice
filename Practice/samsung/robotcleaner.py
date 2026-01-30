import sys

def robotcleaner():
    N, M, r, c, d, room = parse_input()
    solve_robotcleaner(N, M, r, c, d, room)

def solve_robotcleaner(N, M, r, c, d, room):
	moves = [
		# UP
		[-1, 0],
		# LEFT
		[0, -1],
		# DOWN
		[1, 0],
		# RIGHT
		[0, 1],
	]

	# ret = dfs(N, M, r, c, d, room, moves)

	# # print(room)

	# print(ret)
	# return ret

	# DFS NEW
	count = [0]
	dfs_new(N, M, r, c, room, moves, d, count)

	ret = count[0]

	print(ret)
	return ret

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

def dfs_new(N, M, r, c, room, moves, d, count):
	if room[r][c] == 0:
		count[0] += 1
		room[r][c] = 2

	elif room[r][c] == 2:
		# count[0] += 1
		pass

	elif room[r][c] == 1:
		return

	okay = False
	# for move in moves:
	# 	dy, dx = move
	# 	if 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= M-1 and room[r+dy][c+dx] == 0:
	# 		okay = True
	# 		while d_move(d) != move:
	# 			d = rotate_90deg(d)
	# 		break

	for i in range(4):
	    new_d = (d + 3 * (i + 1)) % 4  # 현재 방향에서 반시계로 회전
	    dy, dx = d_move(new_d)[0], d_move(new_d)[1]
	    if 0 <= r + dy <= N-1 and 0 <= c + dx <= M-1 and room[r+dy][c+dx] == 0:
	        okay = True
	        d = new_d
	        break
			
	if okay == True:
		return dfs_new(N, M, r+dy, c+dx, room, moves, d, count)

			# back_dy, back_dx = (-1) * d_move(d)[0], (-1) * d_move(d)[1]
			
			# if room[r+back_dy][c+back_dx] == 1:
			# 	return

	else:
		new_direction = (2 + d) % 4
	
		dy, dx = d_move(new_direction)
	
		return dfs_new(N, M, r+dy, c+dx, room, moves, d, count)



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
		return [0, -1]

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
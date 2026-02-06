import sys

def airpurifier():
    R, C, T, room, air_cleaners = parse_input()
    solve_airpurifier(R, C, T, room, air_cleaners)

def solve_airpurifier(R, C, T, room, air_cleaners):
	for i in range(T):
		dispersed = [ [ 0 for _ in range(C) ] for _ in range(R) ]
		simulate_dispersion(R, C, room, dispersed)
		# if i == 0:
		# 	print('After dispersion')
		# 	print(room)
		simulate_purifier(R, C, room, air_cleaners)
		# if i == 0:
		# 	print('After purification')
		# 	print(room)

	# Get amount of dust in room
	ret = 0
	for i in range(R):
		for j in range(C):
			if room[i][j] > 0:
				ret += room[i][j]

	print(ret)
	return ret

def simulate_dispersion(R, C, room, dispersed):
	moves = [
		[0, 1],
		[1, 0],
		[0, -1],
		[-1, 0]
	]

	for i in range(R):
		for j in range(C):
			if room[i][j] > 0:
				available = []

				for move in moves:
					dy, dx = move
					if 0 <= i + dy and i + dy <= R-1 and 0 <= j + dx and j + dx <= C-1 and room[i+dy][j+dx] != -1:
						available.append([i+dy, j+dx])

				for a in available:
					y, x = a
					dispersed[y][x] += int(room[i][j] / 5)

				room[i][j] -= len(available) * int(room[i][j] / 5)


	for i in range(R):
		for j in range(C):
			if dispersed[i][j] > 0:
				room[i][j] += dispersed[i][j]


def simulate_purifier(R, C, room, air_cleaners):
	# Top purifier
	top_p = sorted(air_cleaners)[0]

	for i in range(top_p[0], 0, -1):
		room[i][0] = room[i-1][0]

	for j in range(0, C-1):
		room[0][j] = room[0][j+1]

	for i in range(0, top_p[0]):
		room[i][C-1] = room[i+1][C-1]

	for j in range(C-1, 1, -1):
		room[top_p[0]][j] = room[top_p[0]][j-1]

	room[top_p[0]][1] = 0

	room[top_p[0]][0] = -1

	# Bottom purifier
	bottom_p = sorted(air_cleaners)[1]

	for i in range(bottom_p[0], R-1):
		room[i][0] = room[i+1][0]

	for j in range(0, C-1):
		room[R-1][j] = room[R-1][j+1]


	for i in range(R-1, bottom_p[0], -1):
		room[i][C-1] = room[i-1][C-1]
	
	for j in range(C-1, 1, -1):
		room[bottom_p[0]][j] = room[bottom_p[0]][j-1]

	room[bottom_p[0]][1] = 0

	room[bottom_p[0]][0] = -1
	

def parse_input():
    input = sys.stdin.readline

    R, C, T = map(int, input().split())

    room = []
    air_cleaners = []

    for i in range(R):
        row = list(map(int, input().split()))
        room.append(row)

        for j, val in enumerate(row):
            if val == -1:
                air_cleaners.append((i, j))

    return R, C, T, room, air_cleaners


# example usage
if __name__ == "__main__":
	airpurifier()
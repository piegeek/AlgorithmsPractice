import sys
import heapq

def babyshark():
    N, space, shark_pos = parse_input()
    solve_babyshark(N, space, shark_pos)

def solve_babyshark(N, space, shark_pos):
	# Initialization 
	shark_size = 2

	ret = dfs(shark_pos, N, space, shark_size, [0])

	print(ret)
	return ret

def dfs(shark_pos, N, space, shark_size, count):
	# print(f'shark_pos: {shark_pos[0]}, {shark_pos[1]}, shark_size: {shark_size}, count: {count}')
	# print(space)

	y, x = shark_pos

	fish_locations = get_fish_locations(space, shark_size)

	if len(fish_locations) == 0:
		return 0

	distance = [ float('inf') for _ in range(len(fish_locations)) ]

	get_distance(distance, fish_locations, shark_pos, N, shark_size, space)

	min_distance = min(distance)

	if distance.count(min_distance) > 1:
		min_indices = [ i for i in range(len(fish_locations)) if distance[i] == min_distance ]
		fish_locations_by_min_distance = [ fish_locations[idx] for idx in min_indices ]

		fish_r_by_min_distance = [ x[0] for x in fish_locations_by_min_distance ]

		min_r = min(fish_r_by_min_distance)

		if fish_r_by_min_distance.count(min_r) > 1:
			min_indices_by_r = [ i for i in min_indices if fish_locations[i][0] == min_r ]
			fish_locations_by_min_r = [ fish_locations[idx] for idx in min_indices_by_r ]

			target = sorted(fish_locations_by_min_r, key = lambda x : x[1])[0]

		else:
			target = sorted(fish_locations_by_min_distance, key = lambda x : x[0])[0]
	else:
		target = fish_locations[distance.index(min_distance)]

	r, c = target
	space[r][c] = 0
	count[0] += 1

	if count[0] == shark_size:
		new_shark_size = shark_size + 1
		count[0] = 0
	else:
		new_shark_size = shark_size

	# return abs(y-r) + abs(x-c) + dfs((r, c), N, space, new_shark_size, count)

	moveable_distance = [float('inf')]
	fish_location = [[r, c]]
	shark_start_pos = [y, x]
	get_distance(moveable_distance, fish_location, shark_start_pos, N, shark_size, space)

	return moveable_distance[0] + dfs((r, c), N, space, new_shark_size, count)

def get_distance(distance, fish_locations, shark_pos, N, shark_size, space):
	moves = [
		[0, 1],
		[1, 0],
		[0, -1],
		[-1, 0]
	]

	visited = [ [ False for _ in range(N) ] for _ in range(N) ]

	queue = []

	y, x = shark_pos

	visited[y][x] = True
	heapq.heappush(queue, [0, y, x])

	while len(queue) > 0:
		dist, r, c = heapq.heappop(queue)
		visited[r][c] = True

		if [r, c] in fish_locations:
			dist_idx = fish_locations.index([r, c])
			distance[dist_idx] = dist

		for move in moves:
			dy, dx = move
			if 0 <= r + dy and r + dy <= N-1 and 0 <= c + dx and c + dx <= N-1 and (space[r+dy][c+dx] == 0 or shark_size >= space[r+dy][c+dx]) and visited[r+dy][c+dx] == False:
				heapq.heappush(queue, [dist+1, r+dy, c+dx])

def get_fish_locations(space, shark_size):
	locations = []
	for i in range(len(space)):
		for j in range(len(space[i])):
			if space[i][j] in range(1, 6+1) and space[i][j] < shark_size:
				locations.append([i, j])

	return locations

def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())

    space = []
    shark_pos = None

    for i in range(N):
        row = list(map(int, input().split()))
        space.append(row)

        for j, val in enumerate(row):
            if val == 9:
                shark_pos = (i, j)
                space[i][j] = 0  # treat shark position as empty

    return N, space, shark_pos


# example usage
if __name__ == "__main__":
	babyshark()
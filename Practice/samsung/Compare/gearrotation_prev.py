import sys

# 🥇 The Golden Rule
# If a decision for one node depends on the original state of another node, you must separate decision and mutation.

def gearrotation():
    gears, rotations = parse_input()
    solve_gearrotation(gears, rotations)

def solve_gearrotation(gears, rotations):
	# Initialization
	polarity = [ False for _ in range(3) ]

	for rotation in rotations:
		visited = [ False for _ in range(4) ]
		idx, direction = rotation

		for i in range(3):
			if gears[i][2] == gears[i+1][6]:
				polarity[i] = True
			else:
				polarity[i] = False

		if direction == 1:
			gears[idx] = gears[idx][1:] + [gears[idx][0]]
		elif direction == -1:
			gears[idx] = [gears[idx][-1]] + gears[idx][0:-1]

		dfs(idx, direction, visited, polarity, gears)

	ret = 0
	for i in range(4):
		if gears[i][0] == 1:
			ret += (2 ** i)

	print(ret)
	return ret


def dfs(idx, direction, visited, polarity, gears):
	if visited[idx] == True:
		return

	visited[idx] = True

	if all_visited(visited):
		return

	neighbors = get_neighbors(idx, visited)

	for neighbor in neighbors:
		didnt_move = False

		polarity_idx = min(idx, neighbor)

		if direction == 1:
			if polarity[polarity_idx] == False:
				gears[neighbor] = [gears[neighbor][-1]] + gears[neighbor][0:-1]
			else:
				didnt_move = True
		elif direction == -1:
			if polarity[polarity_idx] == False:
				gears[neighbor] = gears[neighbor][1:] + [gears[neighbor][0]]
			else:
				didnt_move = True

		if didnt_move:
			continue

		new_direction = (-1) * direction
		
		# Polarity should be only modified once per gear operation -> Can we make it right without this?
		# if neighbor > idx:
		# 	polarity[idx] = (gears[idx][2] == gears[neighbor][6])
		# else:
		# 	polarity[neighbor] = (gears[idx][6] == gears[neighbor][2])

		dfs(neighbor, new_direction, visited, polarity, gears)

	# visited[idx] = False


def all_visited(visited):
	for i in range(len(visited)):
		if visited[i] == False:
			return False

	return True

def get_neighbors(gear_num, visited):
	if gear_num == 0:
		cand = [ 1 ]

	elif gear_num == 1:
		cand = [0, 2]

	elif gear_num == 2:
		cand = [1, 3]

	elif gear_num == 3:
		cand = [2]

	return [ x for x in cand if visited[x] == False ]
	# return cand

def parse_input():
    input = sys.stdin.readline

    gears = []
    for _ in range(4):
        # each line has 8 digits (0 or 1), space-separated or not depending on judge
        line = input().strip().split()
        if len(line) == 1:  # e.g. "10101111"
            gears.append(list(map(int, line[0])))
        else:              # e.g. "1 0 1 0 1 1 1 1"
            gears.append(list(map(int, line)))

    K = int(input().strip())

    rotations = []
    for _ in range(K):
        idx, direction = map(int, input().split())
        rotations.append((idx - 1, direction))  # convert to 0-based index

    return gears, rotations


# example usage
if __name__ == "__main__":
	gearrotation()
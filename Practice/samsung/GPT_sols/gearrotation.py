import sys

# 🥇 The Golden Rule
# If a decision for one node depends on the original state of another node, you must separate decision and mutation.

def gearrotation():
    gears, rotations = parse_input()
    solve_gearrotation(gears, rotations)

def solve_gearrotation(gears, rotations):
	for idx, direction in rotations:
		# 1) polarity snapshot (DO NOT change during DFS)
		polarity = [False] * 3
		for i in range(3):
			polarity[i] = (gears[i][2] != gears[i+1][6])

		visited = [False] * 4
		rotate_dir = [0] * 4

		# 2) DFS to decide rotation directions
		dfs(idx, direction, visited, rotate_dir, polarity)

		# 3) Apply rotations
		for i in range(4):
			if rotate_dir[i] == 1:
				gears[i] = [gears[i][-1]] + gears[i][:-1]
			elif rotate_dir[i] == -1:
				gears[i] = gears[i][1:] + [gears[i][0]]

	ret = 0
	for i in range(4):
		if gears[i][0] == 1:
			ret += (1 << i)

	print(ret)
	return ret

def dfs(idx, direction, visited, rotate_dir, polarity):
	if visited[idx]:
		return

	visited[idx] = True
	rotate_dir[idx] = direction

	for neighbor in get_neighbors(idx):
		p = min(idx, neighbor)

		if not polarity[p]:   # teeth are same → no rotation propagation
			continue

		dfs(neighbor, -direction, visited, rotate_dir, polarity)

def get_neighbors(idx):
	if idx == 0:
		return [1]
	elif idx == 1:
		return [0, 2]
	elif idx == 2:
		return [1, 3]
	else:
		return [2]

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
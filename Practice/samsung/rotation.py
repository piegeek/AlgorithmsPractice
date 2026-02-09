import sys

def rotation():
    N, M, T, disks, operations = parse_input()
    solve_rotation(N, M, T, disks, operations)

def solve_rotation(N, M, T, disks, operations):
	for t in range(T):
		simulate_rotate(disks, operations[t])

		# print(disks)

	ret = get_disks_sum(disks)
	print(ret)
	return ret

def simulate_rotate(disks, ops):
	x_t, d_t, k_t = ops

	for i in range(len(disks)):
		if (i + 1) % x_t == 0:
			rotate_disk(i, disks, d_t, k_t)

	# Simulate removal of duplicates
	if remove_adjacent_duplicates(disks) == False:
		add_and_subtract_1(disks)

def add_and_subtract_1(disks):
	disks_sum = 0
	disks_count = 0

	for i in range(len(disks)):
		for j in range(len(disks[i])):
			if disks[i][j] != -1:
				disks_sum += disks[i][j]
				disks_count += 1

	disks_avg = disks_sum / disks_count

	for i in range(len(disks)):
		for j in range(len(disks[i])):
			if disks[i][j] != 0 and disks[i][j] > disks_avg:
				disks[i][j] -= 1
			elif disks[i][j] != 0 and disks[i][j] < disks_avg:
				disks[i][j] += 1
	

def remove_adjacent_duplicates(disks):
	duplicate_found = False
	for i in range(len(disks)):
		for j in range(len(disks[i])):
			neighbors = get_neighbors(i, j, disks)
			# has_duplicate = False

			duplicates = [[i, j]]

			for neighbor in neighbors:
				r, c = neighbor
				if disks[i][j] == disks[r][c] and disks[i][j] != -1:
					duplicate_found = True
					# has_duplicate = True
					# disks[r][c] = -1

					duplicates_dfs(r, c, disks, duplicates)

			# if has_duplicate:
			# 	disks[i][j] = -1
			if len(duplicates) >= 2:
				for duplicate in duplicates:
					r, c = duplicate
					disks[r][c] = -1

	return duplicate_found

def duplicates_dfs(i, j, disks, duplicates):
	duplicates.append([i, j])

	neighbors = get_neighbors(i, j, disks)

	for neighbor in neighbors:
		r, c = neighbor
		if disks[i][j] != -1 and disks[i][j] == disks[r][c] and [r, c] not in duplicates:
			duplicates_dfs(r, c, disks, duplicates)


def get_neighbors(i, j, disks):
	neighbors = []

	N = len(disks)
	M = len(disks[0])

	if i == 0:
		neighbors.append([1, j])
	elif 1 <= i and i <= N-2:
		neighbors.append([i-1, j])
		neighbors.append([i+1, j])
	elif i == N-1:
		neighbors.append([i-1, j])

	for d in [-1, 1]:
		r, c = i, (j+d) % M
		if [r, c] not in neighbors:
			neighbors.append([r, c])

	return neighbors
			

def rotate_disk(i, disks, d_t, k_t):
	M = len(disks[i])

	if d_t == 0:
		for k in range(k_t):
			temp = disks[i][M-1]
			for j in range(M-1, 0, -1):
				disks[i][j] = disks[i][j-1]
			disks[i][0] = temp

	elif d_t == 1:
		for k in range(k_t):
			temp = disks[i][0]
			for j in range(0, M-1):
				disks[i][j] = disks[i][j+1]
			disks[i][M-1] = temp

def get_disks_sum(disks):
	disks_sum = 0

	for i in range(len(disks)):
		for j in range(len(disks[i])):
			if disks[i][j] != -1:
				disks_sum += disks[i][j]

	return disks_sum

def parse_input():
    input = sys.stdin.readline

    N, M, T = map(int, input().split())

    disks = []
    for _ in range(N):
        disks.append(list(map(int, input().split())))

    operations = []
    for _ in range(T):
        x, d, k = map(int, input().split())
        operations.append((x, d, k))

    return N, M, T, disks, operations


# example usage
if __name__ == "__main__":
	rotation()
import sys

def laboratory():
    N, M, lab, viruses, empty = parse_input()
    solve_laboratory(N, M, lab, viruses, empty)

def solve_laboratory(N, M, lab, viruses, empty):
	ret = 0

	for i in range(N):
		for j in range(M):
			if lab[i][j] == 0:
				lab[i][j] = 1
				ret = max(ret, dfs(lab, 3-1, viruses))
				# Backtracking
				lab[i][j] = 0

	print(ret)
	return ret

def dfs(lab, num, viruses):
	ret = 0

	if num == 0:
		ret = get_maximum_safespace(lab, viruses)
		return ret

	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if lab[i][j] == 0:
				lab[i][j] = 1
				ret = max(ret, dfs(lab, num-1, viruses))
				# Backtracking
				lab[i][j] = 0

	return ret

def get_maximum_safespace(lab, viruses):
	# Propagate
	visited = [ [ False for _ in range(len(lab[0])) ] for _ in range(len(lab)) ]

	for v in viruses:
		y, x = v
		propagate_dfs(y, x, lab, visited)

	safe_count = 0
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if lab[i][j] == 0:
				safe_count += 1

	# Backtracking
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if visited[i][j] == True:
				lab[i][j] = 0

	for v in viruses:
		y, x = v
		lab[y][x] = 2

	return safe_count


def propagate_dfs(y, x, lab, visited):
	N = len(lab)
	M = len(lab[0])

	if visited[y][x] == True: return

	lab[y][x] = 2

	visited[y][x] = True

	moves = [
		# UP
		[-1, 0],
		# RIGHT
		[0, 1],
		# DOWN
		[1, 0],
		# LEFT
		[0, -1]
	]

	for move in moves:
		dy, dx = move
		if 0 <= y + dy and y + dy <= N-1 and 0 <= x + dx and x + dx <= M-1 and lab[y+dy][x+dx] == 0:
			propagate_dfs(y+dy, x+dx, lab, visited)


def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    lab = []
    viruses = []
    empty = []

    for i in range(N):
        row = list(map(int, input().split()))
        lab.append(row)

        for j, cell in enumerate(row):
            if cell == 2:
                viruses.append((i, j))
            elif cell == 0:
                empty.append((i, j))

    return N, M, lab, viruses, empty


# example usage
if __name__ == "__main__":
	laboratory()

import sys

def surveillance():
    N, M, office, cctvs = parse_input()
    solve_surveillance(N, M, office, cctvs)

def solve_surveillance(N, M, office, cctvs):
	direction_one = [
		# RIGHT
		[[0, 1]],
		# DOWN
		[[1, 0]],
		# LEFT
		[[0, -1]],
		# UP
		[[-1, 0]]
	]

	direction_two = [
		# HORIZONTAL
		[ [0, -1], [0, 1] ],
		# VERTICAL
		[ [-1, 0], [1, 0] ]
	]

	direction_three = [
		# NE
		[ [-1, 0], [0, 1] ],
		# SE
		[ [1, 0], [0, 1] ],
		# SW
		[ [1, 0], [0, -1] ],
		# NW
		[ [-1, 0], [0, -1] ]
	]

	direction_four = [
		# EXCEPT DOWN
		[ [0, -1], [-1, 0], [0, 1] ],
		# EXCEPT LEFT
		[ [-1, 0], [0, 1], [1, 0] ],
		# EXCEPT UP
		[ [0, 1], [1, 0], [0, -1] ],
		# EXCEPT RIGHT
		[ [1, 0], [0, -1], [-1, 0] ]
	]

	direction_five = [
		[ [0, 1], [1, 0], [0, -1], [-1, 0] ]
	]

	directions = [ direction_one, direction_two, direction_three, direction_four, direction_five ]

	ret = dfs(0, office, cctvs, directions)

	print(ret)
	return ret

def dfs(idx, office, cctvs, directions):
	# Leaf node
	if idx == len(cctvs):
		print('--------')
		for row in office:
			print(row)
		print('--------')
		return count_blind_spots(office)

	i, j, cctv_type = cctvs[idx]

	direction = directions[cctv_type-1] # 0 - indexing

	ret = float('inf')

	for dir in direction:
		for coord in dir:
			r, c = i, j
			dy, dx = coord[0], coord[1]
			while 0 <= r + dy and r + dy <= (len(office) - 1) and 0 <= c + dx and c + dx <= (len(office[0]) - 1) and office[r+dy][c+dx] != 6:
				if office[r+dy][c+dx] in range(1, 6):
					pass
				else:
					office[r+dy][c+dx] += 9
				r += dy
				c += dx

		# print('--------')
		# for row in office:
		# 	print(row)
		# print('--------')

		ret = min(ret, dfs(idx+1, office, cctvs, directions))

		# Backtracking
		for coord in dir:
			r, c = i, j
			dy, dx = coord[0], coord[1]
			while 0 <= r + dy and r + dy <= (len(office) - 1) and 0 <= c + dx and c + dx <= (len(office[0]) - 1) and office[r+dy][c+dx] != 6:
				if office[r+dy][c+dx] in range(1, 6):
					pass
				else:
					# office[r+dy][c+dx] undoes result of higher branch too. Should be changed like the bottom
					office[r+dy][c+dx] -= 9
				r += dy
				c += dx


	return ret

def count_blind_spots(office):
	count = 0

	for i in range(len(office)):
		for j in range(len(office[i])):
			if office[i][j] == 0:
				count += 1

	return count

def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    office = []
    cctvs = []

    for i in range(N):
        row = list(map(int, input().split()))
        office.append(row)

        for j, cell in enumerate(row):
            if 1 <= cell <= 5:
                cctvs.append((i, j, cell))  # (row, col, type)

    return N, M, office, cctvs


# example usage
if __name__ == "__main__":
	surveillance()
import sys

DOWN = 1
RIGHT = 2

def runway():
    N, L, grid = parse_input()
    solve_runway(N, L, grid)

def solve_runway(N, L, grid):
	ret = 0

	if try_path(0, 0, RIGHT, N, L, grid):
		ret += 1
	if try_path(0, 0, DOWN, N, L, grid):
		ret += 1

	for j in range(1, N):
		if try_path(0, j, DOWN, N, L, grid):
			ret += 1
	
	for i in range(1, N):
		if try_path(i, 0, RIGHT, N, L, grid):
			ret += 1

	print(ret)
	return ret

def try_path(r, c, direction, N, L, grid):
	inclined_plane_placed = [ False for _ in range(N) ]

	inclined_plane_head = -1
	inclined_plane_tail = N

	if direction == DOWN:
		for i in range(N-1):
			# Grid is decreasing
			if grid[i][c] > grid[i+1][c]:
				# Diff by 1 - rule (1 - 2)
				if grid[i][c] == grid[i+1][c] + 1:
					inclined_plane_head = (i+1) + L

					# Plane out of range - rule (2 - 4)
					if inclined_plane_head > N:
						return False

					# Overlap - rule (2 - 1)
					for p in range(i+1, inclined_plane_head):
						if inclined_plane_placed[p] == True:
							return False
						inclined_plane_placed[p] = True

					# Flat floor - rule (1 - 3)
					for x in range(i+1, inclined_plane_head):
						if grid[x][c] != grid[i+1][c]:
							return False
					
				else:
					return False
			# Grid is increasing
			elif grid[i][c] < grid[i+1][c]:
				# Diff by 1 - rule (1 - 2)
				if grid[i][c] + 1 == grid[i+1][c]:
					inclined_plane_tail = (i+1) - L
					
					# Plane out of range - rule (2 - 4)
					if inclined_plane_tail < 0:
						return False

					# Overlap - rule (2 - 1)
					for p in range(inclined_plane_tail, i+1):
						if inclined_plane_placed[p] == True:
							return False
						inclined_plane_placed[p] = True

					# Flat floor - rule (1 - 3)
					for x in range(i+1, inclined_plane_head):
						if grid[x][c] != grid[i+1][c]:
							return False
				else:
					return False
		
	if direction == RIGHT:
		inclined_plane_head = -1

		for j in range(N-1):
			# Grid is decreasing
			if grid[r][j] > grid[r][j+1]:
				# Diff by 1 - rule (1 - 2)
				if grid[r][j] == grid[r][j+1] + 1:
					inclined_plane_head = (j+1) + L

					# Plane out of range - rule (2 - 4)
					if inclined_plane_head > N:
						return False

					# Overlap - rule (2 - 1)
					for p in range(j+1, inclined_plane_head):
						if inclined_plane_placed[p] == True:
							return False
						inclined_plane_placed[p] = True

					# Flat floor - rule (1 - 3)
					for x in range(j+1, inclined_plane_head):
						if grid[r][x] != grid[r][j+1]:
							return False
					
				else:
					return False
			# Grid is increasing
			elif grid[r][j] < grid[r][j+1]:
				# Diff by 1 - rule (1 - 2)
				if grid[r][j] + 1 == grid[r][j+1]:
					inclined_plane_tail = (j+1) - L
					
					# Plane out of range - rule (2 - 4)
					if inclined_plane_tail < 0:
						return False

					# Overlap - rule (2 - 1)
					for p in range(inclined_plane_tail, j+1):
						if inclined_plane_placed[p] == True:
							return False
						inclined_plane_placed[p] = True

					# Flat floor - rule (1 - 3)
					for x in range(j+1, inclined_plane_head):
						if grid[r][x] != grid[r][j+1]:
							return False
				else:
					return False

	return True


def parse_input():
    input = sys.stdin.readline

    N, L = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    return N, L, grid


# example usage
if __name__ == "__main__":
	runway()
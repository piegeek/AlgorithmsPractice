import sys
import copy

def fishing():
    R, C, M, sharks, field = parse_input()
    solve_fishing(R, C, M, sharks, field)

def solve_fishing(R, C, M, sharks, field):
	caught_sharks = []

	for j in range(C):
		simulate_fishing(j, R, C, M, sharks, field, caught_sharks)
		# print('--------------field--------------')
		# for row in field:
		# 	print(row)
		# print('--------------field--------------')
		simulate_shark_movement(R, C, field, sharks)
		# print('--------------field--------------')
		# for row in field:
		# 	print(row)
		# print('--------------field--------------')

	ret = sum(caught_sharks)
	print(ret)
	return ret

def simulate_fishing(t, R, C, M, sharks, field, caught_sharks):
	for i in range(R):
		if len(field[i][t]) > 0:
			# Append size of shark
			caught_sharks.append(field[i][t][0][4])
			shark = field[i][t][0]

			if shark in sharks:
				sharks.remove(shark)

			field[i][t] = []

			break

def simulate_shark_movement(R, C, field, sharks):
	moves = [
		# UP(1)
		[-1, 0],
		# DOWN(2)
		[1, 0],
		# RIGHT(3)
		[0, 1],
		# LEFT(4)
		[0, -1]
	]
	prev_sharks = copy.deepcopy(sharks)

	# Update shark info
	for sh in range(len(sharks)):
		r, c, s, d, z = sharks[sh]
		dy, dx = moves[d-1]

		for amount_moved in range(s):
			if r == R - 1 and d == 2:
				dy *= (-1)
				d = 1
			elif r == 0 and d == 1:
				dy *= (-1)
				d = 2
			if c == C - 1 and d == 3:
				dx *= (-1)
				d = 4
			elif c == 0 and d == 4:
				dx *= (-1)
				d = 3
			
			r += dy
			c += dx

		sharks[sh][0], sharks[sh][1], sharks[sh][2], sharks[sh][3], sharks[sh][4] = r, c, s, d, z

	# Update field based on new info
	for sh in range(len(prev_sharks)):
		prev_shark = prev_sharks[sh]
		r, c, s, d, z = prev_shark
		field[r][c].pop(-1)

	sharks_to_remove = []

	for sh in range(len(sharks)):
		r, c, s, d, z = sharks[sh]

		if len(field[r][c]) > 0:
			prev_shark = field[r][c][0]
			prev_shark_size = prev_shark[4]
			if z > prev_shark_size:
				field[r][c] = [ sharks[sh] ]
				sharks_to_remove.append(prev_shark)
			else:
				sharks_to_remove.append(sharks[sh])
		else:
			field[r][c].append(sharks[sh])

	# Remove sharks from sharks
	for shark in sharks_to_remove:
		if shark in sharks:
			sharks.remove(shark)
		

def parse_input():
    input = sys.stdin.readline

    R, C, M = map(int, input().split())

    field = [ [ [] for _ in range(C) ] for _ in range(R) ]

    sharks = []
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks.append([r - 1, c - 1, s, d, z])  # convert to 0-based (r, c)
        field[r-1][c-1].append([r - 1, c - 1, s, d, z])

    return R, C, M, sharks, field


# example usage
if __name__ == "__main__":
	fishing()
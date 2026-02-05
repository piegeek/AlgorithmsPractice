import sys
import copy

def treeinvestment():
    N, M, K, A, trees = parse_input()
    solve_treeinvestment(N, M, K, A, trees)

def solve_treeinvestment(N, M, K, A, trees):
	ages = [ [ [] for _ in range(N) ] for _ in range(N) ]

	# Initialization
	for i in range(M):
		x, y, age = trees[i]
		ages[x][y].append(age)

	original_A = copy.deepcopy(A)

	for i in range(N):
		for j in range(N):
			A[i][j] = 5

	for i in range(K):
		dead = [ [ 0 for _ in range(N) ] for _ in range(N) ]

		simulate_spring(N, M, K, A, ages, dead)

		# print(f'After spring, ages: {ages}, dead: {dead}')

		simulate_summer(N, M, K, A, ages, dead)

		new_trees = [ [ 0 for _ in range(N) ] for _ in range(N) ]

		simulate_autumn(N, M, K, A, ages, new_trees)
		simulate_winter(N, M, K, A, ages, original_A)

	ret = count_trees(ages)
	print(ret)
	return ret

def count_trees(ages):
	count = 0

	for i in range(len(ages)):
		for j in range(len(ages[i])):
			if len(ages[i][j]) > 0:
				count += len(ages[i][j])

	return count

def simulate_spring(N, M, K, A, ages, dead):
	for i in range(N):
		for j in range(N):
			if len(ages[i][j]) > 0:
				to_die = [ False for _ in range(len(ages[i][j])) ]
				ages[i][j] = sorted(ages[i][j])
				
				for k in range(len(ages[i][j])):
					if A[i][j] < ages[i][j][k]:
						# print('here1')
						to_die[k] = True
						# Add age of dead tree
						dead[i][j] += int(ages[i][j][k] / 2)
					else:
						# print('here2')
						A[i][j] -= ages[i][j][k]
						ages[i][j][k] += 1

				ages[i][j] = [ ages[i][j][k] for k in range(len(ages[i][j])) if to_die[k] == False ]

def simulate_summer(N, M, K, A, ages, dead):
	for i in range(N):
		for j in range(N):
			if dead[i][j] > 0:
				A[i][j] += dead[i][j]


def simulate_autumn(N, M, K, A, ages, new_trees):
	moves = [
		# RIGHT
		[0, 1],
		# DOWN
		[1, 0],
		# LEFT
		[0, -1],
		# UP
		[-1, 0],
		# NE
		[-1, 1],
		# SE
		[1, 1],
		# SW
		[1, -1],
		# NW
		[-1, -1]
	]

	# Decide if we should plant trees adjacently
	for i in range(N):
		for j in range(N):
			if len(ages[i][j]) > 0:
				for k in range(len(ages[i][j])):
					if ages[i][j][k] % 5 == 0:
						for move in moves:
							dy, dx = move
							if 0 <= i + dy and i + dy <= N-1 and 0 <= j + dx and j + dx <= N-1:
								new_trees[i+dy][j+dx] += 1

	
	# Add new trees
	for i in range(N):
		for j in range(N):
			if new_trees[i][j] > 0:
				for k in range(new_trees[i][j]):
					ages[i][j].append(1)

				ages[i][j] = sorted(ages[i][j])

def simulate_winter(N, M, K, A, ages, original_A):
	for i in range(N):
		for j in range(N):
			A[i][j] += original_A[i][j]


def parse_input():
    input = sys.stdin.readline

    N, M, K = map(int, input().split())

    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    trees = []
    for _ in range(M):
        x, y, z = map(int, input().split())
        trees.append((x - 1, y - 1, z))  # convert to 0-based

    return N, M, K, A, trees


# example usage
if __name__ == "__main__":
	treeinvestment()
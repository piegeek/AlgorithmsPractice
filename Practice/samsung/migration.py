import sys

def migration():
    N, L, R, population = parse_input()
    solve_migration(N, L, R, population)

def solve_migration(N, L, R, population):
	ret = dfs(N, L, R, population)
	print(ret)
	return ret

def dfs(N, L, R, population):
	open_borders = [ [ False for _ in range(N) ] for _ in range(N) ]

	for i in range(N-1):
		for j in range(N-1):
			if abs(population[i+1][j] - population[i][j]) in range(L, R+1):
				open_borders[i+1][j] = True
				open_borders[i][j] = True
			if abs(population[i][j+1] - population[i][j]) in range(L, R+1):
				open_borders[i][j+1] = True
				open_borders[i][j] = True
			if abs(population[i+1][j+1] - population[i][j+1]) in range(L, R+1):
				open_borders[i+1][j+1] = True
				open_borders[i][j+1] = True
			if abs(population[i+1][j+1] - population[i+1][j]) in range(L, R+1):
				open_borders[i+1][j+1] = True
				open_borders[i+1][j] = True
	
	# Leaf node - termination condition
	is_leaf_node = True
	for i in range(N):
		for j in range(N):
			if open_borders[i][j] == True:
				is_leaf_node = False
				break

	if is_leaf_node:
		return 0

	visited = [ [ False for _ in range(N) ] for _ in range(N) ]

	for i in range(N):
		for j in range(N):
			if open_borders[i][j] == True and visited[i][j] == False:
				countries = []
				migrate(N, i, j, visited, population, countries, open_borders)

				pop_sum = sum([population[i][j] for [i, j] in countries])
				num_countries = len(countries)

				for y, x in countries:
					population[y][x] = int(pop_sum / num_countries)

	return 1 + dfs(N, L, R, population)

def no_more_migrate(N, L, R, population):
	return False

def migrate(N, i, j, visited, population, countries, open_boarders):
	if visited[i][j] == True:
		return

	countries.append([i, j])

	visited[i][j] = True

	neighbors = [
		# RIGHT
		[i, j+1],
		# DOWN
		[i+1, j],
		# LEFT
		[i, j-1],
		# UP
		[i-1, j]
	]

	for neighbor in neighbors:
		y, x = neighbor
		if 0 <= y and y <= N-1 and 0 <= x and x <= N-1 and open_boarders[y][x] == True and visited[y][x] == False:
			migrate(N, y, x, visited, population, countries, open_boarders)

def parse_input():
    input = sys.stdin.readline

    N, L, R = map(int, input().split())

    population = []
    for _ in range(N):
        population.append(list(map(int, input().split())))

    return N, L, R, population


# example usage
if __name__ == "__main__":
	migration()
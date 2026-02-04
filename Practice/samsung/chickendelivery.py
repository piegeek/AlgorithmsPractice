import sys
import heapq
import copy

def chickendelivery():
    N, M, city, houses, chickens = parse_input()
    solve_chickendelivery(N, M, city, houses, chickens)

def solve_chickendelivery(N, M, city, houses, chickens):
	ret = float('inf')

	for k in range(1, M+1):
		combs = []
		stack = []
		visited = [ [ False for _ in range(N) ] for _ in range(N) ]
		get_combs(chickens, k, stack, combs, visited)

		# print(combs)

		for comb in combs:
			for chicken in chickens:
				# print(f'chicken: {chicken}, comb: {comb}')
				if chicken not in comb:
					y, x = chicken
					city[y][x] = 0


			ret = min(ret, get_total_chicken_distance(N, M, city, houses, chickens))

			# Backtracking
			for chicken in chickens:
				if chicken not in comb:
					y, x = chicken
					city[y][x] = 2

	print(ret)
	return ret


def get_total_chicken_distance(N, M, city, houses, chickens):
	house_chicken_distances = []

	for house in houses:
		r, c = house
		chicken_distance = get_house_chicken_distance(N, M, city, r, c, chickens)
		house_chicken_distances.append(chicken_distance)

		# print(f'r: {r}, c: {c}, distance: {chicken_distance}')

	return sum(house_chicken_distances)


def get_combs(chickens, k, stack, combs, visited):
	if k == 0:
		stack_copy = copy.deepcopy(stack)
		combs.append(stack_copy)
		return 

	for c in range(len(chickens)):
		y, x = chickens[c]
		if visited[y][x] == False:
			visited[y][x] = True
			stack.append([y, x])
			get_combs(chickens, k-1, stack, combs, visited)
			stack.pop(-1)
			visited[y][x] = False

def get_house_chicken_distance(N, M, city, r, c, chickens):
	moves = [
		# RIGHT
		[0, 1],
		# DOWN
		[1, 0],
		# LEFT
		[0, -1],
		# UP
		[-1 ,0]
	]

	queue = []

	heapq.heappush(queue, (0, [r, c]))

	while len(queue) > 0:
		priority, [y, x] = heapq.heappop(queue)

		if city[y][x] == 2:
			return priority

		for move in moves:
			dy, dx = move
			if 0 <= y + dy and y + dy <= N - 1 and 0 <= x + dx and x + dx <= N - 1:
				heapq.heappush(queue, (priority + abs(dy) + abs(dx), [y + dy, x + dx]))



def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    city = []
    houses = []
    chickens = []

    for i in range(N):
        row = list(map(int, input().split()))
        city.append(row)

        for j, cell in enumerate(row):
            if cell == 1:
                houses.append([i, j])
            elif cell == 2:
                chickens.append([i, j])

    return N, M, city, houses, chickens


# example usage
if __name__ == "__main__":
	chickendelivery()
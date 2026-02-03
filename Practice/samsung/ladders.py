import sys
import copy

def ladders():
    N, M, H, ladder = parse_input()
    solve_ladders(N, M, H, ladder)

def solve_ladders(N, M, H, ladder):
	# res = [ 0 for _ in range(N+1) ]
	# simulate(N, M, H, ladder, res)

	# print(res)

	for count in range(0,4):
		combs = []
		visited = [ [ False for _ in range(N+1) ] for _ in range(H+1) ]
		stack = []
		generate_combs(N, M, H, ladder, combs, stack, visited, count)

		# print(combs)

		for comb in combs:
			res = [ 0 for _ in range(N+1) ]
			for coord in comb:
				a, b = coord
				ladder[a][b] = True

			# simulate(N, M, H, ladder, res)
			# if correct(N, res):
			# 	print(count)
			# 	return count

			if simulate_match(N, M, H, ladder):
				print(count)
				return count

			# if sorted(comb) == sorted([(4,2), (1,3), (3,4)]):
			# 	print(res)
			
			# Backtracking
			for coord in comb:
				a, b = coord
				ladder[a][b] = False

	print(-1)
	return -1

def generate_combs(N, M, H, ladder, combs, stack, visited, count):
	if count == 0:
		stack_copy = copy.deepcopy(stack)
		combs.append(stack_copy)
		return

	for i in range(1, H+1):
		# There cant be a horizontal line where col == N
		for j in range(1, N):
			if visited[i][j] == False and ladder[i][j] == False:
				visited[i][j] = True
				stack.append((i, j))
				generate_combs(N, M, H, ladder, combs, stack, visited, count-1)
				# Backtracking
				stack.pop(-1)
				visited[i][j] = False

def correct(N, res):
	for i in range(1, N+1):
		if res[i] != 1: return False

	return True

def simulate(N, M, H, ladder, res):
	for i in range(1, N+1):
		r = 1
		left, curr = i-1, i

		while r <= H:
			if left >= 0 and ladder[r][left] == True:
				# print(f'1, i: {i}, r: {r}, left: {left}, curr: {curr}')
				left, curr = left - 1, left 
				# if 0 <= curr and curr <= N:
				# 	res[curr] += 1

			elif curr <= N and ladder[r][curr] == True:
				# print(f'2, i: {i}, r: {r}, left: {left}, curr: {curr}')
				left, curr = curr, curr + 1
				# if 0 <= curr and curr <= N:
				# 	res[curr] += 1

			r += 1

		if 0 <= curr and curr <= N:
			res[curr] += 1

def simulate_match(N, M, H, ladder):
	for i in range(1, N+1):
		r = 1
		left, curr = i-1, i

		while r <= H:
			if left >= 0 and ladder[r][left] == True:
				left, curr = left - 1, left 

			elif curr <= N and ladder[r][curr] == True:
				left, curr = curr, curr + 1

			r += 1

		if curr != i:
			return False

	return True

def parse_input():
    input = sys.stdin.readline

    N, M, H = map(int, input().split())

    # ladder[a][b] == True means
    # at height a, vertical line b is connected to b+1
    ladder = [[False] * (N + 1) for _ in range(H + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        ladder[a][b] = True

    return N, M, H, ladder


# example usage
if __name__ == "__main__":
	ladders()
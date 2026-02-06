import sys
import copy
import heapq

def laboratory3():
    N, M, lab, virus_candidates, empty_count = parse_input()
    solve_laboratory3(N, M, lab, virus_candidates, empty_count)

def solve_laboratory3(N, M, lab, virus_candidates, empty_count):
	if empty_count == 0:
		print(0)
		return 0

	combs_m = []
	stack = []
	visited = [ False for _ in range(len(virus_candidates)) ]
	get_combs(virus_candidates, M, stack, combs_m, visited)
	
	# print(combs_m)

	ret = float('inf')

	for comb in combs_m:
		ret = min(ret, get_prop_time(N, comb, lab, empty_count))

	if ret == float('inf'):
		print(-1)
		return -1

	else:
		print(ret)
		return ret


def get_prop_time(N, comb, lab_setting, empty_count):
	lab = copy.deepcopy(lab_setting)

	queue = []

	moves = [
		[0, 1],
		[1, 0],
		[0, -1],
		[-1, 0]
	]

	for pos in comb:
		r, c = pos
		lab[r][c] = 3
		heapq.heappush(queue, [1, r, c])

	while len(queue) > 0:
		t, r, c = heapq.heappop(queue)

		if empty_count == 0:
			return t

		for move in moves:
			dy, dx = move
			if 0 <= r + dy and r + dy <= N - 1 and 0 <= c + dx and c + dx <= N - 1 and lab[r+dy][c+dx] != 1 and lab[r+dy][c+dx] != 3:
				if lab[r+dy][c+dx] == 0:
					empty_count -= 1

				lab[r+dy][c+dx] = 3

				heapq.heappush(queue, [t+1, r+dy, c+dx])

	return float('inf')

# How to find all combinations without duplicates -> Force ordering (idea in duplicate situation)
def get_combs(virus_candidates, M, stack, combs_m, visited):
	# if M == 0:
	# 	stack_copy = copy.deepcopy(stack)
	# 	combs_m.append(stack_copy)

	for i in range(len(virus_candidates) - M + 1):
		stack.append(virus_candidates[i])
		dfs(i, virus_candidates, M-1, stack, combs_m)
		stack.pop(-1)

	# neighbors = [ idx for idx in range(len(virus_candidates)) if visited[idx] == False ]

	# for neighbor in neighbors:
	# 	visited[neighbor] = True
	# 	stack.append(virus_candidates[neighbor])
	# 	get_combs(virus_candidates, M-1, stack, combs_m, visited)
	# 	stack.pop(-1)
	# 	visited[neighbor] = False

def dfs(idx, virus_candidates, M, stack, combs_m):
	if idx == len(virus_candidates) or M == 0:
		stack_copy = copy.deepcopy(stack)
		combs_m.append(stack_copy)

	for i in range(idx+1, len(virus_candidates)):
		stack.append(virus_candidates[i])
		dfs(i, virus_candidates, M-1, stack, combs_m)
		stack.pop(-1)


def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    lab = []
    virus_candidates = []
    empty_count = 0

    for i in range(N):
        row = list(map(int, input().split()))
        lab.append(row)

        for j, cell in enumerate(row):
            if cell == 2:
                virus_candidates.append([i, j])
            elif cell == 0:
                empty_count += 1

    return N, M, lab, virus_candidates, empty_count


# example usage
if __name__ == "__main__":
	laboratory3()
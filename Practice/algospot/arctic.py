import sys
import math

def arctic():
    C, test_cases = parse_input()

    for N, coords in test_cases:
        solve_arctic(N, coords)

# O(n * 2^n) complexity expected
def solve_arctic(N, coords):
	cache = {}

	visited = [ False for _ in range(N) ]

	ret = float('inf')

	for i in range(N):
		visited[i] = True
		ret = min(ret, dfs(i, visited, coords, cache)[1])
		visited[i] = False

	print(ret)
	return ret

def dfs(idx, visited, coords, cache):
	visited_state = get_visited_state(visited)

	if (idx, visited_state) in cache: return cache[(idx, visited_state)]

	if visited.count(False) == 2:
		indices = [ i for i in range(len(coords)) if visited[i] == False ]

		return indices[0], math.sqrt(
			(coords[indices[0]][0] - coords[indices[1]][0]) ** 2
			+
			(coords[indices[0]][1] - coords[indices[1]][1]) ** 2
		)

	indices = [ i for i in range(len(coords)) if i != idx and visited[i] == False ]

	min_output = float('inf')
	root = None

	results = []

	for index in indices:
		visited[index] = True
		res = dfs(index, visited, coords, cache)

		results.append(res)

		visited[index] = False

	output = []

	for res in results:
		root, D = res

		output.append(max(distance(idx, root, coords), D))

	cache[(idx, visited_state)] = (idx, min(output))
	return idx, min(output)

def get_visited_state(visited):
	visited_state = ''
	for v in visited:
		if v == True:
			visited_state += '1'
		else:
			visited_state += '0'

	return visited_state

def distance(idx, root, coords):
	return math.sqrt(
		(coords[idx][0] - coords[root][0]) ** 2 +
		(coords[idx][1] - coords[root][1]) ** 2
	)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of bases
        N = int(input().strip())

        # Coordinates of bases
        coords = []
        for _ in range(N):
            x, y = map(float, input().split())
            coords.append((x, y))

        test_cases.append((N, coords))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	arctic()
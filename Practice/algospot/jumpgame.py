import sys
import heapq

def jumpgame():
    C, test_cases = parse_input()
    for n, grid in test_cases:
        print(solve_jumpgame(n, grid))

def solve_jumpgame(n, grid):
	reachable = False

	origin = [0, 0]

	queue = []

	heapq.heappush(queue, origin)

	while len(queue) > 0:
		coord = heapq.heappop(queue)

		# Check if endpoint reached
		if coord == [n-1, n-1]:
			reachable = True
			break

		val = grid[coord[0]][coord[1]]

		right_r, right_c = coord[0], coord[1] + val

		# Check within boundaries
		if right_c <= len(grid[0]) - 1:
			heapq.heappush(queue, [right_r, right_c])

		down_r, down_c = coord[0] + val, coord[1]

		# Check within boundaries
		if down_r <= len(grid) - 1:
			heapq.heappush(queue, [down_r, down_c])

	if reachable:
		return 'YES'
	else:
		return 'NO'

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Grid size (2 ≤ n ≤ 100)
        n = int(input().strip())

        grid = []
        for _ in range(n):
            row = list(map(int, input().split()))
            assert len(row) == n
            grid.append(row)

        test_cases.append((n, grid))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	jumpgame()

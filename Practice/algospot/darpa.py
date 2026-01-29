import sys

def darpa():
    C, test_cases = parse_input()

    for N, M, positions in test_cases:
        solve_darpa(N, M, positions)

def solve_darpa(N, M, positions):
	min_distance = float('inf')

	min_distances = []
	
	for i in range(0, M - N + 1):
		dfs(i, N - 1, M, positions, min_distance, min_distances)

	ret = max(min_distances)

	print(ret)
	return ret


def dfs(idx, cam_nums, M, positions, min_distance, min_distances):
	# Base case
	if cam_nums == 0:
		min_distances.append(min_distance)
		return

	for i in range(idx+1, M - cam_nums + 1):
		distance = positions[i] - positions[idx]
		dfs(i, cam_nums - 1, M, positions, min(min_distance, distance), min_distances)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of cameras and candidate relay stations
        N, M = map(int, input().split())

        # Positions of possible camera locations (floats, sorted)
        positions = list(map(float, input().split()))
        assert len(positions) == M

        test_cases.append((N, M, positions))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	darpa()
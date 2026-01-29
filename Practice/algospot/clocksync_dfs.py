import sys
import copy

# Order of pressing switches shouldn't matter; dfs offers better solution with max complexity of 4^10; length of queue in bfs solution blows up 10^n
# When there is a fixed number of branches that should be considered, dfs can be a viable solution
def clocksync():
	C, test_cases = parse_input()

	for clocks in test_cases:
		depths = []
		solve_clocksync(clocks, 0, depths, 0)
		if len(depths) == 0: print(-1)
		else: print(min(depths))

def solve_clocksync(clocks, depth, depths, total_presses):
	# Convert all 12 oclocks to 0 oclock
	for i in range(len(clocks)):
		if clocks[i] == 12:
			clocks[i] = 0

	switches = {
		'0': [0, 1, 2],
		'1': [3, 7, 9, 11],
		'2': [4, 10, 14, 15],
		'3': [0, 4, 5, 6, 7],
		'4': [6, 7, 8, 10, 12],
		'5': [0, 2, 14, 15],
		'6': [3, 14, 15],
		'7': [4, 5, 7, 14, 15],
		'8': [1, 2, 3, 4, 5],
		'9': [3, 4, 5, 9, 13]
	}

	# Base case; leaf node
	if all_synced(clocks):
		depths.append(total_presses)
		return

	if depth > 9: return

	for i in range(4):
		# Manipulation
		adjust = switches[str(depth)]

		clocks_copy = copy.deepcopy(clocks)

		for idx in adjust:
			clocks[idx] = (clocks[idx] + (3 * i)) % 12

		solve_clocksync(clocks, depth+1, depths, total_presses+i)

		# Backtracking
		clocks = clocks_copy


def all_synced(clocks):
	synced = True

	for clock in clocks:
		if clock != 0:
			synced = False
	
	return synced

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (<= 30)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Each test case consists of 16 integers in one line
        clocks = list(map(int, input().split()))
        assert len(clocks) == 16
        test_cases.append(clocks)

    return C, test_cases


# Example usage
if __name__ == "__main__":
    clocksync()
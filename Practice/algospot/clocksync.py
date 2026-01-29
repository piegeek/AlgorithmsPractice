import sys
import heapq
import copy

def clocksync():
	C, test_cases = parse_input()

	for clocks in test_cases:
		solve_clocksync(clocks)

def solve_clocksync(clocks):
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

	queue = []

	step = 1

	for switch in switches.keys():
		adjust = switches[switch]

		needs_to_change = get_needs_to_change(clocks)

		if has_intersection(adjust, needs_to_change):
			clocks_copy = copy.deepcopy(clocks)

			for idx in adjust:
				clocks_copy[idx] = (clocks_copy[idx] + 3) % 12

			priority = 0

			for i in range(len(clocks)):
				priority += abs(clocks_copy[i] - clocks[i]) 

			heapq.heappush(queue, (priority, [step, clocks_copy]))

	while len(queue) > 0:
		priority, [curr_step, curr_clocks] = heapq.heappop(queue)

		if all_synced(curr_clocks):
			print(curr_step)
			return

		# If returned to original configuration after multiple manipulations
		if curr_clocks == clocks:
			continue

		for switch in switches.keys():
			adjust = switches[switch]

			needs_to_change = get_needs_to_change(curr_clocks)

			if has_intersection(adjust, needs_to_change):
				clocks_copy = copy.deepcopy(curr_clocks)

				for idx in adjust:
					clocks_copy[idx] = (clocks_copy[idx] + 3) % 12

				new_priority = priority

				for i in range(len(clocks)):
					new_priority += abs(clocks_copy[i] - curr_clocks[i])

				heapq.heappush(queue, (new_priority, [curr_step + 1, clocks_copy]))

	return -1

def has_intersection(arr1, arr2):
	for i in range(len(arr1)):
		if arr1[i] in arr2:
			return True

	return False

def get_needs_to_change(clocks):
	needs_to_change = []

	for i in range(len(clocks)):
		if clocks[i] != 0:
			needs_to_change.append(i)

	return needs_to_change

		
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

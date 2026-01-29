import sys
import heapq

def pi():
	C, test_cases = parse_input()

	for string in test_cases:
		print(solve_pi(string))

def solve_pi(string):
	queue = []

	lengths = [3,4,5]

	difficulties = []

	for length in lengths:
		heapq.heappush(queue, (get_difficulty(string[0:length]), length))

	while len(queue) > 0:
		difficulty, idx = heapq.heappop(queue)

		# Termination condition; Base cases; remainders of mod3 overlaps with mod4, mod5 - thus only 3 cases needed
		if idx == len(string) - 1 or idx == len(string) or idx == len(string) - 2:
			difficulties.append(difficulty)

		for length in lengths:
			if idx + length <= len(string):
				heapq.heappush(queue, (difficulty + get_difficulty(string[idx:idx+length]), idx + length))

	return min(difficulties)


def get_difficulty(string):
	if all_equal(string): return 1
	if all_diff_by_one(string): return 2
	if alternating(string): return 4
	if arithemtic_sequence(string): return 5
	
	return 10

def all_equal(string):
	first_char = string[0]

	for i in range(len(string)):
		if string[i] != first_char:
			return False

	return True

def all_diff_by_one(string):
	num_list = list(map(int, list(string)))

	diff_by_one = True
	diff_by_minus_one = True

	# Diff by 1
	for i in range(1, len(string)):
		if num_list[i] - num_list[i-1] != 1:
			diff_by_one = False

	# Diff by -1
	for i in range(1, len(string)):
		if num_list[i] - num_list[i-1] != -1:
			diff_by_minus_one = False

	return diff_by_one or diff_by_minus_one

def alternating(string):
	first_char = string[0]
	second_char = string[1]

	for i in range(len(string)):
		if i % 2 == 0:
			if string[i] != first_char: return False
		if i % 2 != 0:
			if string[i] != second_char: return False

	return True

def arithemtic_sequence(string):
	num_list = list(map(int, list(string)))

	d = num_list[1] - num_list[0]

	for i in range(1, len(string)):
		if num_list[i] - num_list[i-1] != d: return False

	return True


def parse_input():
	input = sys.stdin.readline

	C = int(input().strip())
	test_cases = []

	for _ in range(C):
		test_cases.append(input().strip())

	return C, test_cases

if __name__ == '__main__':
	pi()
# Correctness of algorithm??
import sys

def wildcard():
    C, test_cases = parse_input()
    for W, N, filenames in test_cases:
        solve_wildcard(W, N, filenames)

def solve_wildcard(W, N, filenames):
	# 'hea?pi*fy*que*ue'
	# 'healpiblahfyblahqueblahue'
	# ['heap?pi', 'fy', 'que', 'ue']

	valid = []

	tokens = []

	for split_str in W.split('*'):
		tokens.append(split_str)

	for filename in filenames:
		if len(filename) < len(W):
			continue

		is_valid_filename = True
		star_count = 1

		filename_idx = 0
		for i in range(len(W)):
			if filename_idx == len(filename):
				break

			if W[i] != filename[filename_idx]:
				if W[i] == '?':
					pass
				elif W[i] == '*':
					token = tokens[star_count]

					if token == '':
						star_count += 1
						filename_idx += 1
						continue

					filename_idx = filename[i+1:].find(token)

					if filename_idx == -1:
						is_valid_filename = False
						break

					else:
						star_count += 1
						filename_idx += i
				else:
					is_valid_filename = False
					break

			filename_idx += 1

		if filename_idx < len(filename):
			is_valid_filename = False

		if is_valid_filename:
			valid.append(filename)

	valid = sorted(valid)

	for valid_filename in valid:
		print(valid_filename)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (1 ≤ C ≤ 10)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Wildcard pattern string
        W = input().strip()

        # Number of filenames
        N = int(input().strip())

        filenames = []
        for _ in range(N):
            filename = input().strip()
            filenames.append(filename)

        test_cases.append((W, N, filenames))

    return C, test_cases


if __name__ == "__main__":
	wildcard()

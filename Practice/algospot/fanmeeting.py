import sys

def fanmeeting():
    C, test_cases = parse_input()
    for members, fans in test_cases:
        print(solve_fanmeeting(members, fans))
	
def solve_fanmeeting(members, fans):
	window_size = len(members)

	if window_size > len(fans):
		return 0

	count = 0

	for i in range(len(fans) - window_size + 1):
		window = fans[i:i+window_size]

		all_hugged = True

		for j in range(window_size):
			if window[j] == 'M' and members[j] == 'M':
				all_hugged = False
				break

		if all_hugged:
			count += 1
	
	return count


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 20)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Gender string of members
        members = input().strip()

        # Gender string of fans
        fans = input().strip()

        test_cases.append((members, fans))

    return C, test_cases


if __name__ == "__main__":
	fanmeeting()

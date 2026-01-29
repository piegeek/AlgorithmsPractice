import sys

def matchorder():
    C, test_cases = parse_input()

    for N, russian, korean in test_cases:
        solve_matchorder(N, russian, korean)

def solve_matchorder(N, russian, korean):
	sorted_russian = sorted(russian)
	sorted_korean = sorted(korean)

	ret = 0

	for i in range(N):
		# shifted_russian = sorted_russian[-i:] + sorted_russian[:-i]
		shifted_korean = sorted_korean[-i:] + sorted_korean[:-i]

		# print(shifted_russian)
		# print(shifted_korean)

		ret = max(ret, get_max_match(sorted_russian, shifted_korean))

	print(ret)

def get_max_match(sorted_russian, shifted_korean):
	count = 0
	for i in range(len(sorted_russian)):
		if shifted_korean[i] >= sorted_russian[i]:
			count += 1

	return count

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of players per team
        N = int(input().strip())

        # Russian team ratings (in fixed order)
        russian = list(map(int, input().split()))
        assert len(russian) == N

        # Korean team ratings (unordered)
        korean = list(map(int, input().split()))
        assert len(korean) == N

        test_cases.append((N, russian, korean))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	matchorder()
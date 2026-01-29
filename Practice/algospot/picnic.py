def picnic():
	test_cases = parse_input()

	for n, pairs in test_cases:
		solve_picnic(n, pairs)

def solve_picnic(n, pairs):
	adjacency_list = create_adjacency_list(n, pairs)

	# print(adjacency_list)

	matched = [ False for _ in range(n) ]

	count =	try_match(adjacency_list, matched)

	print(count)

def try_match(adjacency_list, matched):
	# All matched - leaf node
	if False not in matched:
		return 1

	count = 0

	first_not_matched = matched.index(False)

	# Backtracking
	matched[first_not_matched] = True

	for friend in adjacency_list[first_not_matched]:
		if matched[friend] == False:
			matched[friend] = True
			count += try_match(adjacency_list, matched)
			matched[friend] = False

	matched[first_not_matched] = False

	return count


def create_adjacency_list(n, pairs):
	adjacency_list = [ [] for _ in range(n) ]

	for pair in pairs:
		v1, v2 = pair[0], pair[1]

		adjacency_list[v1].append(v2)
		adjacency_list[v2].append(v1)

	return adjacency_list
	

def parse_input():
    C = int(input().strip())  # number of test cases
    test_cases = []

    for _ in range(C):
        # Read n (students) and m (friend pairs)
        n, m = map(int, input().split())

        # Read m pairs of friends
        pairs = []

        friends = list(map(int, input().strip().split()))

        for i in range(m):
            a, b = friends[2*i], friends[2*i+1]
            pairs.append((a, b))

        test_cases.append((n, pairs))

    return test_cases


if __name__ == '__main__':
	picnic()
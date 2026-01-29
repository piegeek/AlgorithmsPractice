import sys

def potion():
    c, test_cases = parse_input()

    for n, r, p in test_cases:
        solve_potion(n, r, p)

def solve_potion(n, r, p):
	if all_less(r, p):
		ret = [ r[i] - p[i] for i in range(n) ]
		ret = list(map(str, ret))
		print(' '.join(ret))
		return ret

	exceeded_indices = [ i for i in range(n) if p[i] > r[i] ]

	add_arr = []

	for idx in exceeded_indices:
		others = [ i for i in range(n) if i != idx ]
		add = [ 0 for i in range(n) ]

		# Try without adding to idx
		no_adding = True
		add[idx] = 0

		for other_idx in others:
			rate = r[other_idx] / r[idx]

			to_add = rate * p[idx] - p[other_idx]

			if to_add != int(to_add):
				no_adding = False
				break

			add[other_idx] = int(to_add)

		if no_adding:
			add_arr.append(add)
			break

		add = [ 0 for i in range(n) ]
		# Try multiplying and adding
		mult = int(p[idx] / r[idx]) + 1
		add[idx] = mult * r[idx] - p[idx]

		for other_idx in others:
			add[other_idx] = mult * r[other_idx] - p[other_idx]

		add_arr.append(add)

	ret = sorted(add_arr, key = lambda x : sum(x))[0]
	ret = list(map(str, ret))
	print(' '.join(ret))
	return ret


def all_less(r, p):
	for i in range(len(r)):
		if p[i] > r[i]:
			return False

	return True

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Number of ingredients
        n = int(input().strip())

        # Required amounts ri
        r = list(map(int, input().split()))
        assert len(r) == n

        # Already added amounts pi
        p = list(map(int, input().split()))
        assert len(p) == n

        test_cases.append((n, r, p))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	potion()
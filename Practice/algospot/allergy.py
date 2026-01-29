import sys

def allergy():
    T, test_cases = parse_input()

    for n, m, friends, foods in test_cases:
        solve_allergy(n, m, friends, foods)

def solve_allergy(n, m, friends, foods):
	visited = 0
	cache = {}
	ret = min_foods(0, visited, friends, foods, cache, n, m)

	print(ret)

	return ret

def min_foods(idx, visited, friends, foods, cache, n, m):
	# Leaf node
	if idx == m:
		return m

	if visited == ((1 << n) - 1):
		return 0

	if (idx, visited) in cache: return cache[(idx, visited)]

	min_food_num = m 

	# Food idx not okay
	min_food_num = min(
		min_food_num,
		min_foods(idx+1, visited, friends, foods, cache, n, m)
	)

	# Food idx okay
	for i in range(len(friends)):
		if friends[i] in foods[idx]:
			visited |= (1 << i)
	
	min_food_num = min(
		min_food_num,
		min_foods(idx+1, visited, friends, foods, cache, n, m) + 1
	)

	cache[(idx, visited)] = min_food_num
	return min_food_num


def parse_input():

    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # Number of friends and foods
        n, m = map(int, input().split())

        # Friend names
        friends = input().split()
        assert len(friends) == n

        # Food information
        foods = []
        for _ in range(m):
            line = input().split()
            cnt = int(line[0])
            eaters = line[1:]
            assert len(eaters) == cnt
            foods.append(eaters)

        test_cases.append((n, m, friends, foods))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	allergy()
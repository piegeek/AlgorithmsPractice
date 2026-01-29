import sys

def canadatrip():
    T, test_cases = parse_input()

    for N, K, cities in test_cases:
        solve_canadatrip(N, K, cities)

def solve_canadatrip(N, K, cities):
	# Brute force
	locations = []

	for L, M, G in cities:
		start = L - M
		loc = start
		
		while loc <= L:
			locations.append(loc)
			loc += G

	locations = sorted(locations)

	print(locations[K - 1])
	return locations[K - 1]

	# Decision and optimize -> Find out how to do
	# max_loc = max([x[0] for x in cities])
	# ret = optimize(K, cities, max_loc)

	# print(ret)
	# return ret

def decision(K, cities, lo, hi):
	count = 0
	for L, M, G in cities:
		start = L - M
		loc = start

		while loc <= L:
			if lo <= loc and loc < hi:
				count += 1

			loc += G

	return K >= count

def optimize(K, cities, max_loc):
	lo = 0
	hi = max_loc

	for it in range(100+1):
		mid = (lo + hi) / 2

		# location of K is greater than midpoint
		if decision(K, cities, lo, mid):
			lo = mid
		# location of K is smaller than midpoint
		else:
			hi = mid

	return hi


def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # Number of cities and K
        N, K = map(int, input().split())

        cities = []
        for _ in range(N):
            L, M, G = map(int, input().split())
            cities.append((L, M, G))

        test_cases.append((N, K, cities))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	canadatrip()
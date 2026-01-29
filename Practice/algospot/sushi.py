import sys

# import sys
# sys.setrecursionlimit(10000000)

def sushi():
    c, test_cases = parse_input()

    for n, m, sushi in test_cases:
        solve_sushi(n, m, sushi)

def solve_sushi(n, m, sushi):
	cache = {}
	pref = dfs(0, n, m, sushi, cache)

	print(pref)

def dfs(idx, n, m, sushi, cache):
	# print(f'idx: {idx}, m: {m}')

	if m < 0:
		return 0
	
	if idx == n:
		return 0

	if (idx, m) in cache: return cache[(idx, m)]

	# if sushi[idx][0] > m: return 0
	ret = 0

	# With item at idx
	if sushi[idx][0] <= m:
		ret = max(ret, sushi[idx][1] + dfs(idx, n, m-sushi[idx][0], sushi, cache))

	# Without item at idx
	without_idx = dfs(idx+1, n, m, sushi, cache)
	ret = max(ret, without_idx)

	cache[(idx, m)] = ret
	return ret


def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # n: number of sushi types, m: budget
        n, m = map(int, input().split())

        sushi = []
        for _ in range(n):
            price, preference = map(int, input().split())
            sushi.append((price, preference))

        test_cases.append((n, m, sushi))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	sushi()
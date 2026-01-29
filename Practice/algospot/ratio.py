import sys

def ratio():
    T, test_cases = parse_input()

    for N, M in test_cases:
        solve_ratio(N, M)

def solve_ratio(N, M):
	MAX_NUM_GAMES = 2000000000
	lo = 0
	hi = MAX_NUM_GAMES

	for it in range(100+1):
		mid = (lo + hi) // 2

		if win_rate_diff(mid, N, M) > 0: # This is the invariant; we modify hi; thus return hi
			hi = mid
		else:
			lo = mid

	if hi == MAX_NUM_GAMES:
		print(-1)
		return -1
	else:
		print(hi)
		return hi 
		
def win_rate_diff(x, N, M):
	return int(((M + x) / (N + x)) * 100) - int((M / N) * 100)

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    T = int(input().strip())
    test_cases = []

    for _ in range(T):
        # N = number of games played, M = number of wins
        N, M = map(int, input().split())
        test_cases.append((N, M))

    return T, test_cases


# Example usage
if __name__ == "__main__":
	ratio()

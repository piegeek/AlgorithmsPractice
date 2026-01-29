import sys

def genius():
    C, test_cases = parse_input()

    # Debug print
    for N, K, M, lengths, transition, favorites in test_cases:
        solve_genius(N, K, M, lengths, transition, favorites)

def solve_genius(N, K, M, lengths, transition, favorites):
	# prob = [0 for _ in range(M)]
	# dfs(0, K, M, lengths, transition, prob, 1)

	# rearranged_prob = []

	# for f in favorites:
	# 	rearranged_prob.append(prob[f])

	rearranged_prob = []

	for f in favorites:
		cache = {}
		# Always starts at song 0
		if f == 0:
			rearranged_prob.append(dfs_memo(0, K, lengths, transition, cache, f))
		else:
			# rearranged_prob.append(dfs_memo(f, K - lengths[0], lengths, transition, cache, f))
			rearranged_prob.append(dfs_memo(0, K, lengths, transition, cache, f))

	print(rearranged_prob)

# Variables: idx, K, prob, parent_prob -> Memoization impossible ? 
def dfs(idx, K, M, lengths, transition, prob, parent_prob):
	# Leaf node
	if K + 0.5 < lengths[idx]:
		prob[idx] += parent_prob
		return

	for i in range(M):
		dfs(i, K - lengths[idx], M, lengths, transition, prob, parent_prob * transition[idx][i])

def dfs_memo(idx, K, lengths, transition, cache, favorite):
	if idx == favorite and K + 0.5 < lengths[idx]:
		cache[(idx, K)] = 1
		return 1
	elif idx != favorite and K + 0.5 < lengths[idx]:
		cache[(idx, K)] = 0
		return 0

	if (idx, K) in cache: return cache[(idx, K)]

	ret = 0

	for i in range(len(lengths)):
		if (K + 0.5) - lengths[idx] >= 0:
			ret += dfs_memo(i, K - lengths[idx], lengths, transition, cache, favorite) * transition[idx][i]

	cache[(idx, K)] = ret
	return ret

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # N: number of songs, K: total time, M: number of favorite songs
        N, K, M = map(int, input().split())

        # Song lengths (minutes)
        L = list(map(int, input().split()))
        assert len(L) == N

        # Transition probability matrix T (NxN)
        T = []
        for _ in range(N):
            row = list(map(float, input().split()))
            assert len(row) == N
            T.append(row)

        # Favorite song indices
        Q = list(map(int, input().split()))
        assert len(Q) == M

        # test_cases.append({
        #     "N": N,
        #     "K": K,
        #     "M": M,
        #     "lengths": L,
        #     "transition": T,
        #     "favorites": Q
        # })

        test_cases.append(
        	[N, K, M, L, T, Q]
        )

    return C, test_cases


# Example usage
if __name__ == "__main__":
	genius()
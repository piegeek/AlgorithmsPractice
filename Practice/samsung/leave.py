import sys

def leave():
    N, T, P = parse_input()
    solve_leave(N, T, P)

def solve_leave(N, T, P):
	T = T[1:]
	P = P[1:]

	ret = 0

	cache = {}

	for i in range(N):
		if (i+1) + T[i] <= (N+1):
			ret = max(ret, dfs(i, N, T, P, cache)) 

	print(ret)
	return ret

def dfs(idx, N, T, P, cache):
	if idx == N:
		return 0

	if idx in cache: return cache[idx]

	ret = P[idx]
	
	for i in range(idx+T[idx], N):
		if (i+1) + T[i] <= (N+1):
			ret = max(ret, dfs(i, N, T, P, cache) + P[idx]) 

	cache[idx] = ret
	return ret

def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())

    T = [0] * (N + 1)
    P = [0] * (N + 1)

    for day in range(1, N + 1):
        T[day], P[day] = map(int, input().split())

    return N, T, P


# example usage
if __name__ == "__main__":
	leave()
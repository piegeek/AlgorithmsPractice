import sys
import copy

def startandlink():
    N, S = parse_input()
    solve_startandlink(N, S)

def solve_startandlink(N, S):
	k = N / 2

	combs = []
	stack = []

	for i in range(1, N+1):
		if (N-i+1) >= k:
			stack.append(i)
			dfs(i, N, k-1, stack, combs)
			stack.pop(-1)

	ret = float('inf')
	
	for comb in combs:
		other_team = [ x for x in range(1, N+1) if x not in comb ]
		ability_sum_1 = 0
		ability_sum_2 = 0
		
		for i in comb:
			for j in comb:
				if i != j:
					ability_sum_1 += S[i-1][j-1]
		
		for i in other_team:
			for j in other_team:
				if i != j:
					ability_sum_2 += S[i-1][j-1]

		ret = min(ret, abs(ability_sum_1 - ability_sum_2))

	print(ret)
	return ret


def dfs(idx, N, k, stack, combs):
	# Leaf node
	if k == 0:
		stack_copy = copy.deepcopy(stack)
		combs.append(stack_copy)
		return 


	for i in range(idx+1, N+1):
		if (N-i+1) >= k:
			stack.append(i)
			dfs(i, N, k-1, stack, combs)
			stack.pop(-1)


def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())

    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))

    return N, S


# example usage
if __name__ == "__main__":
	startandlink()
import sys
import copy

def jlis():
    c, test_cases = parse_input()
    for n, m, A, B in test_cases:
        solve_jlis(n, m, A, B)

def solve_jlis(n, m, A, B):
	# stack_a = []
	# stack_b = []

	# lis_a = get_lis(A, stack_a)
	# lis_b = get_lis(B, stack_b)

	# print(lis_a)
	# print(lis_b)

	# jlis_set = set()

	# for a in lis_a:
	# 	jlis_set.add(a)

	# for b in lis_b:
	# 	jlis_set.add(b)

	# return len(jlis_set)

	joint = A + B

	ret = 0

	cache = {}

	for i in range(len(joint)):
		ret = max(ret, dfs(i, joint, cache))

	print(ret)
	return ret

def dfs(idx, joint, cache):
	if idx == len(joint): return 0

	if idx in cache: return cache[idx]

	ret = 1

	for i in range(idx+1, len(joint)):
		if joint[i] > joint[idx]:
			ret = max(ret, dfs(i, joint, cache) + 1)

	cache[idx] = ret
	return ret

# Check implementation of this code
def get_lis(arr, stack):
	# Base case
	if len(arr) == 1:
		lis = []
		
		stack.append(arr[0])

		if len(stack) > len(lis):
			lis = copy.deepcopy(stack)
		
		stack.pop(-1)

		return lis

	ret = []

	for i in range(len(arr)):
		if arr[0] < arr[i]:
			stack.append(arr[0])

			lis = get_lis(arr[i:], stack)

			if len(lis) > len(ret):
				ret = lis

			stack.pop(-1)

	return ret

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (1 ≤ c ≤ 50)
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Lengths of arrays A and B (1 ≤ n, m ≤ 100)
        n, m = map(int, input().split())

        # Elements of array A
        A = list(map(int, input().split()))
        assert len(A) == n

        # Elements of array B
        B = list(map(int, input().split()))
        assert len(B) == m

        test_cases.append((n, m, A, B))

    return c, test_cases


if __name__ == "__main__":
	jlis()
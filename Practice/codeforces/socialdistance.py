def socialdistance():
	C, test_cases = parse_input()
	for i in range(C):
		n, k, s = test_cases[i]
		print(solve_socialdistance(n, k, s))

def solve_socialdistance(n, k, s):
	s_list = list(map(int, list(s)))

	ret = dp(0, s_list, n, k, s)

	return ret

def dp(idx, s_list, n, k, s):
	if idx == len(s_list):
		return 0

	ret = 0
	
	# Skip idx
	ret = dp(idx+1, s_list, n, k, s)

	# Take idx
	if s_list[idx] == 0 and len([x for x in s_list[max(0, idx-k):min(len(s_list), idx+k+1)] if x == 1]) == 0:
		s_list[idx] = 1
		ret = max(ret, 1 + dp(idx+1, s_list, n, k, s))
		s_list[idx] = 0

	return ret

def parse_input():
	C = int(input())

	test_cases = []

	for _ in range(C):
		n, k = tuple(map(int, input().split()))
		s = str(input())

		test_cases.append([n, k, s])

	return C, test_cases

if __name__ == '__main__':
	socialdistance()
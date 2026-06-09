# F. The Cake Is a Lie

import sys

sys.setrecursionlimit(10 ** 6)

# Simulation + Greedy
def pancakes():
	C, test_cases = parse_input()

	for i in range(C):
		n, a, b, k = test_cases[i]
		print(solve_pancakes_dp(n, a, b, k))

def solve_pancakes_dp(n, a, b, k):
	if n >= 2:
		pans = [0, 0]
	else:
		pans = [0]

	ret = dp(0, pans, n, a, b, k)

	return ret

# Inaccurate results for input: 100 1 2 2
def dp(times, pans, n, a, b, k):
	# print(f'times: {times}')
	print(pans)

	if times == n: return 0

	ret = 0

	# Operation 1
	if len(pans) == 2 and pans[0] < k:
		pans[0] += a
		pans[1] += b
		ret = max(ret, dp(times, pans, n, a, b, k))
		pans[0] -= a
		pans[1] -= b
	
	if len(pans) == 1 and pans[0] < k:
		pans[0] += a
		ret = max(ret, dp(times, pans, n, a, b, k))
		pans[0] -= a

	# Operation 2
	if times < n - 1:
		temp = pans.pop(0)
		pans.append(0)
		if temp == k:
			ret = max(ret, 1 + dp(times + 1, pans, n, a, b, k))
		# elif temp > k:
		else:
			ret = max(ret, dp(times + 1, pans, n, a, b, k))

		pans[0], pans[1] = pans[1], pans[0]
		pans[0] = temp

	if times == n - 1:
		temp = pans.pop(0)
		if temp == k:
			ret = max(ret, 1 + dp(times + 1, pans, n, a, b, k))
		# elif temp > k:
		else:
			ret = max(ret, dp(times + 1, pans, n, a, b, k))
		pans.append(temp)

	return ret

# This seems to work but it's inefficient -> This is currently greedy (dp frontier collapses to 1)
def dp_prev(times, pans, n, a, b, k):
	# print(f'times: {times}')
	# print(pans)

	if times == n:
		return 0

	ret = 0

	if len(pans) == 1 and pans[0] < k:
		pans[0] += a
		ret = max(ret, dp(times, pans, n, a, b, k))
		pans[0] -= a

	if len(pans) == 1 and pans[0] == k:
		temp = pans.pop(0)
		ret = max(ret, 1 + dp(times + 1, pans, n, a, b, k))
		pans.append(temp)

	if len(pans) == 1 and pans[0] > k:
		temp = pans.pop(0)
		ret = max(ret, dp(times + 1, pans, n, a, b, k))
		pans.append(temp)
	
	# What if pans[0] + a > k ? How should we handle those cases?
	
	if len(pans) == 2 and pans[0] < k:
		pans[0] += a
		pans[1] += b
		ret = max(ret, dp(times, pans, n, a, b, k))
		pans[0] -= a
		pans[1] -= b

	if len(pans) == 2 and pans[0] == k:
		if times < n - 1:
			temp = pans.pop(0)
			pans.append(0)
			ret = max(ret, 1 + dp(times + 1, pans, n, a, b, k))
			pans[1] = pans[0]
			pans[0] = temp
		elif times == n - 1:
			temp = pans.pop(0)
			ret = max(ret, 1 + dp(times + 1, pans, n, a ,b, k))
			pans.append(temp)
			pans[0], pans[1] = pans[1], pans[0]

	if len(pans) == 2 and pans[0] > k:
		if times < n - 1:
			temp = pans.pop(0)
			pans.append(0)
			ret = max(ret, dp(times + 1, pans, n, a, b, k))
			pans[1] = pans[0]
			pans[0] = temp
		elif times == n - 1:
			temp = pans.pop(0)
			ret = max(ret, dp(times + 1, pans, n, a, b, k))
			pans.append(temp)

	return ret

def solve_pancakes(n, a, b, k):
	pans = []

	cooked = 0
	ret = 0

	if n == 1:
		pans.append(0)

	while cooked < n:
		# Event 1
		if len(pans) > 0 and pans[0] == k:
			ret += 1
			pans.pop(0)
			pans.append(0)
			cooked += 1
		# Event 2
		elif len(pans) > 0 and pans[0] > k:
			pans.pop(0)
			pans.append(0)
			cooked += 1

		if len(pans) == 2:
			pans[0] += a
			pans[1] += b

		elif len(pans) == 1:
			if cooked < n:
				pans.append(0)
				cooked += 1
			else:
				pans[0] += a

		elif len(pans) == 0:
			if cooked + 2 <= n:
				pans.append(0)
				pans.append(0)
				cooked += 2
			elif cooked + 1 <= n:
				pans.append(0)
				cooked += 1

	return ret


def parse_input():
	C = int(input())

	test_cases = []

	for _ in range(C):
		test_cases.append(list(map(int, input().split(' '))))

	return C, test_cases

if __name__ == '__main__':
	pancakes()
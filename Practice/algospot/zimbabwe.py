import sys
import copy

def zimbabwe():
    c, test_cases = parse_input()
    for e, m in test_cases:
        solve_zimbabwe(e, m)

# What this solution differs from the book's solution
def solve_zimbabwe(e, m):
	# Brute force; too slow
	# perms = []
	# get_perms(e, perms)

	# # print(perms)

	# # Filter out permutations; smaller, no duplicates
	# possible = []

	# for perm in perms:
	# 	price = int(''.join(perm))
	# 	if price < e and price not in possible:
	# 		possible.append(price)
	
	# count = 0

	# for price in possible:
	# 	if price % m == 0:
	# 		count += 1

	# print(count)

	# Another solution
	# e_list = list(str(e))

	# start = int(''.join(sorted(e_list)))

	# count = 0

	# first_multiplier_found = False

	# while start < e:
	# 	# if start % m == 0 and sorted(list(str(start))) == sorted(e_list):
	# 	# if first_multiplier_found == False and start % m == 0:
	# 	# 	first_multiplier_found = True
			
	# 	# if start % m == 0 and sorted(list(str(start))) == sorted(e_list):
	# 	# 	count += 1

	# 	# if first_multiplier_found:
	# 	# 	start += m
	# 	# else:
	# 	# 	start += 1

	# 	start += 1
	# 	count += 1

	# print(count)

	# Dynamic Programming solution
	original_e = list(str(e))
	sorted_e = sorted(list(str(e)))

	indices = {}

	for digit in sorted_e:
		if digit not in indices:
			indices[digit] = sorted_e.index(digit)

	visited = [ False for i in range(len(sorted_e)) ]

	first_digit = sorted_e[0]
	indices[first_digit] += 1
	less = False
	ret = dfs_dp(0, visited, indices, (int(first_digit) % m), less, sorted_e, original_e, m)

	print(ret)
	return ret

	# Dynamic Programming book solution
	# e_copy = copy.deepcopy(e)
	# e = list(str(e))
	# sorted_e = sorted(list(str(e_copy)))

	# cache = {}

	# visited = 0
	# less = False
	# mod = int(e[0]) % m
	# ret = dfs_dp_book(0, visited, mod, less, e, sorted_e, m, cache)

	# print(ret)
	# return ret


'''
But that assumption only holds if all smaller indices of 1 were used.

That is accidentally true here, but it is not guaranteed in general, because:

indices tracks usage count per value

visited tracks usage per index

These two structures can diverge
'''

def dfs_dp(idx, visited, indices, mod, less, sorted_e, original_e, m):
	if idx == len(visited):
		if less and mod == 0: return 1
		else: return 0

	# Filtered out visited indices
	unvisited_indices = [ i for i in range(len(visited)) if visited[i] == False ]

	neighbors = [ int(indices[sorted_e[ui]]) for ui in unvisited_indices if indices[sorted_e[ui]] < len(visited) ]

	count_sum = 0

	for neighbor in neighbors:
		# Filtered out if makes greater number
		if less or original_e[idx] > sorted_e[neighbor]:
			indices[sorted_e[neighbor]] += 1
			visited[neighbor] = True
			new_mod = int(10 * mod + int(sorted_e[neighbor])) % m
			new_less = less or original_e[idx] > sorted_e[neighbor]
			count_sum += dfs_dp(idx+1, visited, indices, new_mod, new_less, sorted_e, original_e, m)

			# Backtracking 
			visited[neighbor] = False
			indices[sorted_e[neighbor]] -= 1

	return count_sum

'''
It directly enforces the invariant:

“You may only use the k-th copy of a digit if the (k−1)-th copy was already used.”

This is index-based, not value-count-based.

Your approach tries to infer index usage from value counts.
That inference is not stable under DFS ordering.
'''
def dfs_dp_book(idx, visited, mod, less, e, sorted_e, m, cache):
	if idx == len(e):
		return 1 if less and (mod == 0) else 0

	if (visited, mod, less) in cache: return cache[(visited, mod, less)]

	ret = 0

	for next in range(0, len(e)):
		if (visited & (1 << next)) == 0:
			# Dont add if makes greater number
			if not less and e[idx] < sorted_e[next]:
				continue

			# Dont visit index if the same digit at a smaller index is not added
			if next > 0 and sorted_e[next - 1] == sorted_e[next] and (visited & (1 << (next - 1))) == 0:
				continue

			next_visited = visited | (1 << next)
			next_mod = int(10 * mod + int(sorted_e[next])) % m
			next_less = less or e[idx] > sorted_e[next]
			ret += dfs_dp_book(idx+1, next_visited, next_mod, next_less, e, sorted_e, m, cache)

	cache[(visited, mod, less)] = ret
	return ret

def get_state(visited):
	state = 0
	for i in range(len(visited)):
		if visited[i] == True:
			state |= (1 << i)

	return state

def get_perms(e, perms):
	letters = list(str(e))

	stack = []

	visited = [False for _ in range(len(letters))]

	for i in range(len(letters)):
		# Pruning
		if letters[i] <= letters[0]:
			dfs(i, letters, stack, len(letters), perms, visited)

def dfs(idx, letters, stack, N, perms, visited):
	if visited[idx] == True:
		return
	
	visited[idx] = True
	stack.append(letters[idx])

	# Pruning
	if int(''.join(stack)) > int(''.join(letters[:len(stack)])):
		# Backtracking
		visited[idx] = False
		stack.pop(-1)
		return
	
	if len(stack) == N:
		print(int(''.join(stack)))
		stack_copy = copy.deepcopy(stack)
		perms.append(stack_copy)

		# Backtracking
		visited[idx] = False
		stack.pop(-1)
		return

	neighbors = [i for i in range(len(letters)) if visited[i] == False]

	for i in neighbors:
		dfs(i, letters, stack, N, perms, visited)

	# Backtracking
	visited[idx] = False
	stack.pop(-1)


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (c ≤ 50)
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Two natural numbers e and m
        # e: 1 ≤ e ≤ 10^14
        # m: 2 ≤ m ≤ 20
        e, m = map(int, input().split())
        test_cases.append((e, m))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	zimbabwe()
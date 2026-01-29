import sys
import heapq

def strjoin():
    c, test_cases = parse_input()

    for n, lengths in test_cases:
        solve_strjoin(n, lengths)

# Had help from book solving this problem
def solve_strjoin(n, lengths):
	# Pruning approach -> Suboptimal solution; can we prove it?
	# min_length = min(lengths)
	# visited = [False for _ in range(n)]
	# min_prices = []
	# for i in range(len(lengths)):
	# 	if lengths[i] == min_length:
	# 		dfs(i, visited, lengths, 0, -lengths[i], min_prices)

	# print(min(min_prices))

	# Divide & Conquer approach
	# sorted_lengths = sorted(lengths)

	# sum_stack = []

	# divide_and_conquer(0, n, sorted_lengths, sum_stack)

	# print(sum(sum_stack))

	# Greedy approach -> Use priority queue
	lengths = sorted(lengths)
	queue = []

	ret = 0
	
	for length in lengths:
		heapq.heappush(queue, (length, length))

	while len(queue) > 1:
		length_a, a = heapq.heappop(queue)
		length_b, b = heapq.heappop(queue)

		ret += (length_a + length_b)

		heapq.heappush(queue, (length_a + length_b, a+b))

	print(ret)
	return ret
				

# Tree height: O(n) -> Not optimal; We can make it O(logn) by divide & conquer
def dfs(idx, visited, lengths, curr_len, len_sum, min_prices):
	# print(f'idx: {idx}, curr_len: {curr_len}, len_sum: {len_sum}')
	if visited[idx] == True:
		return

	visited[idx] = True

	curr_len += lengths[idx]
	len_sum += curr_len

	if all_visited(visited): 
		# print(f'idx: {idx}, curr_len: {curr_len}, len_sum: {len_sum}')
		min_prices.append(len_sum)
		# Throrough backtracking
		visited[idx] = False
		return

	neighbors = [i for i in range(len(lengths)) if visited[i] == False]

	min_length = min([lengths[i] for i in range(len(lengths)) if visited[i] == False])

	for neighbor in neighbors:
		# Pruning
		if lengths[neighbor] == min_length:
			dfs(neighbor, visited, lengths, curr_len, len_sum, min_prices)

	# Backtracking
	visited[idx] = False

def divide_and_conquer(start, end, sorted_lengths, sum_stack):
	# Base case
	if end - start == 2:
		ret_sum = sorted_lengths[start] + sorted_lengths[start+1]
		sum_stack.append(ret_sum)
		return ret_sum

	if end - start < 2:
		return 0

	mid_point = start + (end - start) // 2

	if (end - start) % 2 == 0:
		ret_sum = divide_and_conquer(start, mid_point, sorted_lengths, sum_stack) + divide_and_conquer(mid_point, end, sorted_lengths, sum_stack)
		sum_stack.append(ret_sum)
		return ret_sum

	else:
		# Hard coding -> Doesn't work well; elegant way to solve problem?
		first_two_sum = sorted_lengths[start] + sorted_lengths[start+1]
		sum_stack.append(first_two_sum)

		last_and_first_two_sum = sorted_lengths[start] + sorted_lengths[start+1] + sorted_lengths[end-1]
		sum_stack.append(last_and_first_two_sum)

		ret_sum = divide_and_conquer(start+2, end-1, sorted_lengths, sum_stack) + last_and_first_two_sum
		sum_stack.append(ret_sum)
		return ret_sum

def all_visited(visited):
	for i in range(len(visited)):
		if visited[i] == False:
			return False

	return True


def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Number of strings
        n = int(input().strip())

        # Lengths of the strings
        lengths = list(map(int, input().split()))
        assert len(lengths) == n

        test_cases.append((n, lengths))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	strjoin()
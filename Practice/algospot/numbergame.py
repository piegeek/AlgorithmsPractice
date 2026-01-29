import sys

def numbergame():
    C, test_cases = parse_input()

    for n, board in test_cases:
        solve_numbergame(n, board)

def solve_numbergame(n, board):
	# h_scores = []
	# s_scores = []
	# dfs(n, board, True, 0, 0, h_scores, s_scores, 0, n-1)

	# print(h_scores)
	# print(s_scores)

	# print(f'length: {len(h_scores)}')

	# diff = []
	# for i in range(len(h_scores)):
	# 	diff.append(h_scores[i] - s_scores[i])

	# print(max(diff))

	cache = {}

	score_diff = dfs_dp(n, board, True, 0, n-1, cache)

	ret = score_diff[0] - score_diff[1]
	print(ret)
	return ret

def dfs(n, board, h_turn, h_score, s_score, h_scores, s_scores, left_pointer, right_pointer):
	# Base case
	if left_pointer >= right_pointer:
		h_scores.append(h_score)
		s_scores.append(s_score)
		return

	if right_pointer - left_pointer == 1:
		if h_turn:
			dfs(n, board, False, h_score + board[left_pointer], s_score, h_scores, s_scores, left_pointer + 1, right_pointer)
		else:
			dfs(n, board, True, h_score, s_score + board[left_pointer], h_scores, s_scores, left_pointer + 1, right_pointer)

		return

	# OPTION 1
	if h_turn:
		dfs(n, board, False, h_score + board[left_pointer], s_score, h_scores, s_scores, left_pointer + 1, right_pointer)
	else:
		dfs(n, board, True, h_score, s_score + board[left_pointer], h_scores, s_scores, left_pointer + 1, right_pointer)

	# OPTION 2
	if h_turn:
		dfs(n, board, False, h_score + board[right_pointer], s_score, h_scores, s_scores, left_pointer, right_pointer - 1)
	else:
		dfs(n, board, True, h_score, s_score + board[right_pointer], h_scores, s_scores, left_pointer, right_pointer - 1)

	# OPTION 3
	if right_pointer - left_pointer >= 2:
		dfs(n, board, not h_turn, h_score, s_score, h_scores, s_scores, left_pointer + 2, right_pointer)

	# OPTION 4
	if right_pointer - left_pointer >= 2:
		dfs(n, board, not h_turn, h_score, s_score, h_scores, s_scores, left_pointer, right_pointer - 2)

def dfs_dp(n, board, h_turn, left, right, cache):
	# Leaf node
	if left == right:
		if h_turn:
			return [board[left], 0]
		else:
			return [0, board[left]]

	if (h_turn, left, right) in cache: return cache[(h_turn, left, right)]

	game_results = []

	l_res = dfs_dp(n, board, not h_turn, left + 1, right, cache)

	if h_turn:
		game_results.append([l_res[0] + board[left], l_res[1]])
	else:
		game_results.append([l_res[0], l_res[1] + board[left]])

	r_res = dfs_dp(n, board, not h_turn, left, right - 1, cache)

	if h_turn:
		game_results.append([r_res[0] + board[right], r_res[1]])
	else:
		game_results.append([r_res[0], r_res[1] + board[right]])

	if right - left >= 2:
		le_res = dfs_dp(n, board, not h_turn, left + 2, right, cache)

		if h_turn:
			game_results.append([le_res[0], le_res[1]])
		else:
			game_results.append([le_res[0], le_res[1]])

		re_res = dfs_dp(n, board, not h_turn, left, right - 2, cache)

		if h_turn:
			game_results.append([re_res[0], re_res[1]])
		else:
			game_results.append([re_res[0], re_res[1]])

	if h_turn:
		ret = sorted(game_results, key = lambda x : x[0] - x[1])[-1]
	else:
		ret = sorted(game_results, key = lambda x : x[1] - x[0])[-1]
	
	cache[(h_turn, left, right)] = ret
	return ret


def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        n = int(input().strip())
        board = list(map(int, input().split()))
        test_cases.append((n, board))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	numbergame()
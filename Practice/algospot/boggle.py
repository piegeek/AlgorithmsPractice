def boggle():
	test_cases = parse_input()

	for board, words in test_cases:
		solve_boggle(board, words)

def solve_boggle(board, words):
	prefix_set = set()

	for word in words:
		for x in range(len(word)+1):
			prefix_set.add(word[:x])

	word_dict = {}

	for word in words:
		word_dict[word] = False

	visited = [ [ False for col in row ] for row in board ]

	for i in range(len(board)):
		for j in range(len(board[i])):
			dfs(board, i, j, visited, prefix_set, word_dict, board[i][j])

	# Print out results
	for word in words:
		if word_dict[word] == True:
			print(word + ' ' + 'YES')
		else:
			print(word + ' ' + 'NO')

def dfs(board, i, j, visited, prefix_set, word_dict, current_word):
	# if visited[i][j] == True: return

	if current_word not in prefix_set: return

	# Edge case - if word is already found but can be a part of another word in the same path - how to handle?
	if current_word in word_dict.keys():
		word_dict[current_word] = True
		return

	# If all words are found
	all_found = True
	for word in word_dict.keys():
		if word_dict[word] == False:
			all_found = False
		
	if all_found == True:
		return

	# visited[i][j] = True

	neighbors = get_neighbors(board, i, j)

	for neighbor in neighbors:
		r, c = neighbor[0], neighbor[1]

		dfs(board, r, c, visited, prefix_set, word_dict, current_word + board[r][c])

	# Backtracking
	# visited[i][j] = False


def get_neighbors(board, i, j):
	neighbors = []

	# Up
	if i > 0:
		neighbors.append([i-1, j])
	# Upper right
	if i > 0 and j < len(board[0]) - 1:
		neighbors.append([i-1, j+1])
	# Right
	if j < len(board[0]) - 1:
		neighbors.append([i, j+1])
	# Lower right
	if i < len(board) - 1 and j < len(board[0]) - 1:
		neighbors.append([i+1, j+1])
	# Down
	if i < len(board) - 1:
		neighbors.append([i+1, j])
	# Lower left
	if i < len(board) - 1 and j > 0:
		neighbors.append([i+1, j-1])
	# Left
	if j > 0:
		neighbors.append([i, j-1])
	# Upper left
	if i > 0 and j > 0:
		neighbors.append([i-1, j-1])
	
	return neighbors


def parse_input():
    C = int(input().strip())  # number of test cases
    test_cases = []

    for _ in range(C):
        # Read 5x5 boggle board
        board = []
        for _ in range(5):
            row = input().strip()
            board.append(list(row))  # convert string to list of characters

        # Read number of words
        N = int(input().strip())

        # Read words
        words = []
        for _ in range(N):
            words.append(input().strip())

        test_cases.append((board, words))

    return test_cases

if __name__ == '__main__':
	boggle()
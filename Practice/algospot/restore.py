import sys

def restore():
    C, test_cases = parse_input()
    for k, pieces in test_cases:
        solve_restore(k, pieces)

def solve_restore(k, pieces):
	possible = []

	visited = [False for _ in range(k)]

	for i in range(k):
		dfs(i, k, pieces, visited, possible, 1, '')

	possible = sorted(possible, key=lambda x : len(x))

	print(possible[0])

def dfs(idx, k, pieces, visited, possible, count, prefix):
	visited[idx] = True

	next = pieces[idx]

	overlap_len = -1

	for j in range(min(len(prefix), len(next))):
		if prefix[-1-j:] == next[:j+1]:
			overlap_len = max(overlap_len, j+1)

	if overlap_len == -1:
		if next not in prefix: 
			word = prefix + next
		else:
			word = prefix
	else: word = prefix + next[overlap_len:]

	if count == k:
		possible.append(word)
		# Backtracking
		visited[idx] = False
		return

	neighbors = [i for i in range(k) if visited[i] == False]

	for neighbor in neighbors:
		dfs(neighbor, k, pieces, visited, possible, count+1, word)

	visited[idx] = False



def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of substrings
        k = int(input().strip())

        pieces = []
        for _ in range(k):
            s = input().strip()
            pieces.append(s)

        test_cases.append((k, pieces))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	restore()
import sys

def tiling2():
    C, test_cases = parse_input()
    for n in test_cases:
        # print(solve_tiling2_dfs(n))
        print(solve_tiling2(n))

# How to setup recurrence relation
def solve_tiling2(n):
	if n == 1: return 1
	if n == 2: return 2
	if n == 3: return 3

	DIVIDOR = 1000000007

	if n % 2 == 0:
		return (solve_tiling2(n/2) ** 2 + solve_tiling2((n-2)/2) ** 2) % DIVIDOR
	else:
		return (solve_tiling2((n-1)/2) ** 2 + 2 * solve_tiling2((n-1)/2) * solve_tiling2((n-3)/2)) % DIVIDOR

def solve_tiling2_dfs(n):
	table = [ [ False for _ in range(n) ] for _ in range(2) ]

	directions = [
		[0, 1],
		[1, 0]
	]

	count = [0]

	dfs(n, table, 0, 0, directions, count)

	return count[0]

def dfs(n, table, y, x, directions, count):
	for i in range(2):
		for j in range(n):
			if table[i][j] == False:
				fail_count = 0
				can_fill = False
				for direction in directions:
					dy, dx = direction[0], direction[1]
					if i + dy in range(2) and j + dx in range(n) and table[i+dy][j+dx] == False:
						table[i][j] = True
						table[i+dy][j+dx] = True

						if dfs(n, table, i+dy, j+dx, directions, count):
							can_fill = True

						# Backtracking
						table[i][j] = False
						table[i+dy][j+dx] = False
					else:
						fail_count += 1

				if fail_count == 2 or can_fill == False:
					return False

	count[0] += 1
	# print(count[0])
	return True

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Each test case has one natural number n (1 ≤ n ≤ 100)
        n = int(input().strip())
        test_cases.append(n)

    return C, test_cases


# Example usage
if __name__ == "__main__":
	tiling2()
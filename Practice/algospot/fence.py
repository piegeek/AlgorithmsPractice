import sys

def fence():
	C, test_cases = parse_input()
	for N, heights in test_cases:
		print(solve_fence(N, heights))

def solve_fence(N, heights):
	max_area = float('-inf')

	for i in range(N):
		height = heights[i]

		taller_than = [ False for _ in range(N) ]

		for j in range(N):
			if heights[j] >= height:
				taller_than[j] = True

		# [T, F, T, T, T, T, F]
		count = 0
		counts = []
		for j in range(N):
			if taller_than[j] == False:
				counts.append(count)
				count = 0
				continue
			
			count += 1

		# print(counts)
		
		if len(counts) == 0:
			max_area = max(max_area, height * 1)
		else:
			max_area = max(max_area, height * max(counts))

	return max_area


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Number of boards (1 ≤ N ≤ 20000)
        N = int(input().strip())

        # Heights of the boards (N non-negative integers ≤ 10000)
        heights = list(map(int, input().split()))
        assert len(heights) == N

        test_cases.append((N, heights))

    return C, test_cases


if __name__ == "__main__":
	fence()
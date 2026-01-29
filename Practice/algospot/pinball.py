import sys

def pinball():
    C, test_cases = parse_input()

    for x, y, dx, dy, N, obstacles in test_cases:
        solve_pinball(x, y, dx, dy, N, obstacles)

def solve_pinball(x, y, dx, dy, N, obstacles):
	pass

def parse_input():
    input = sys.stdin.readline

    # Number of test cases
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        # Ball position, direction, number of obstacles
        x, y, dx, dy, N = map(int, input().split())

        obstacles = []
        for _ in range(N):
            xi, yi, ri = map(int, input().split())
            obstacles.append((xi, yi, ri))

        test_cases.append((x, y, dx, dy, N, obstacles))

    return C, test_cases


# Example usage
if __name__ == "__main__":
	pinball()
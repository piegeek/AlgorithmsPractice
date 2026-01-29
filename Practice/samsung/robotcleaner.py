import sys

def robotcleaner():
    N, M, r, c, d, room = parse_input()
	solve_robotcleaner(N, M, r, c, d, room)

def solve_robotcleaner(N, M, r, c, d, room):
	pass

def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    r, c, d = map(int, input().split())

    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))

    return N, M, r, c, d, room


# example usage
if __name__ == "__main__":
	robotcleaner()
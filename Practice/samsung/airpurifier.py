import sys

def airpurifier():
    R, C, T, room, air_cleaners = parse_input()
    solve_airpurifier(R, C, T, room, air_cleaners)

def solve_airpurifier(R, C, T, room, air_cleaners):
	pass

def parse_input():
    input = sys.stdin.readline

    R, C, T = map(int, input().split())

    room = []
    air_cleaners = []

    for i in range(R):
        row = list(map(int, input().split()))
        room.append(row)

        for j, val in enumerate(row):
            if val == -1:
                air_cleaners.append((i, j))

    return R, C, T, room, air_cleaners


# example usage
if __name__ == "__main__":
	airpurifier()
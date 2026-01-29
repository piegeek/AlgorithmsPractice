import sys

def tetromino():
    N, M, paper = parse_input()
    solve_tetromino(N, M, paper)

def solve_tetromino(N, M, paper):
	shapes = [
		# SHAPE1
		[ [0,0], [0,1], [0,2], [0,3] ],
		[ [0,0], [1,0], [2,0], [3,0] ],
		# SHAPE2
		[ [0,0], [0,1], [1,0], [1,1] ],
		# SHAPE3-1
		[ [0,0], [1,0], [2,0], [2,1] ],
		[ [0,0], [0,1], [1,1], [2,1] ],
		[ [0,0], [1,0], [1,-1], [1,-2] ],
		[ [0,0], [0,1], [0,2], [1,0] ],
		# SHAPE3-2
		[ [0,0], [1,0], [2,0], [2,-1] ],
		[ [0,0], [0,1], [0,2], [1,2] ],
		[ [0,0], [1,0], [1,1], [1,2] ],
		[ [0,0], [0,1], [1,0], [2,0] ],
		# SHAPE4
		[ [0,0], [1,0], [1,1], [2,1] ],
		[ [0,0], [0,1], [1,-1], [1,0] ],
		[ [0,0], [1,0], [1,-1], [2,-1] ],
		[ [0,0], [0,1], [1,1], [1, 2] ],
		# SHAPE5
		[ [0,0], [0,1], [0,2], [1,1] ],
		[ [0,0], [1,0], [1,-1], [2,0] ],
		[ [0,0], [1,-1], [1,0], [1,1] ],
		[ [0,0], [1,0], [1,1], [2,0] ]
	]

	ret = 0

	for i in range(N):
		for j in range(M):
			for shape in shapes:
				can_place_shape = True
				for coord in shape:
					dy, dx = coord[0], coord[1]

					if not (0 <= i + dy and i + dy <= N-1 and 0 <= j + dx and j + dx <= M-1):
						can_place_shape = False
						break

				if can_place_shape:
					shape_sum = 0
					for coord in shape:
						dy, dx = coord[0], coord[1]
						shape_sum += paper[i+dy][j+dx]
					
					ret = max(ret, shape_sum)
	
	print(ret)
	return ret

def parse_input():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))

    return N, M, paper


# example usage
if __name__ == "__main__":
	tetromino()
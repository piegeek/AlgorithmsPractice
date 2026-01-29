import sys

def quadtree():
	C, quadtrees = parse_input()
	for q in quadtrees:
		print(solve_quadtree(q))

def solve_quadtree(tree):
	# Base cases
	if len(tree) == 1: return tree
	if len(tree) == 5: return 'x' + tree[2+1] + tree[3+1] + tree[0+1] + tree[1+1]

	stack = []
	count = 0

	for i in range(len(tree)):

		t = tree[i]

		if count == 4:
			fourth = stack.pop(-1)
			third = stack.pop(-1)
			second = stack.pop(-1)
			first = stack.pop(-1)
			x = stack.pop(-1)

			merged_string = x + third + fourth + first + second

			stack.append(merged_string)

			for j in range(len(stack) - 1, -1, -1):
				if stack[j] == 'x':
					count = (len(stack) - 1) - j
					break
		
		if t == 'x':
			stack.append(t)
			count = 0
		elif i == len(tree) - 1 and len(stack) == 4:
			stack.append(t)
			break
		elif (t == 'w' or t == 'b') and count < 4:
			stack.append(t)
			count += 1

	if count == 4:
		fourth = stack.pop(-1)
		third = stack.pop(-1)
		second = stack.pop(-1)
		first = stack.pop(-1)
		x = stack.pop(-1)
		
		merged_string = x + third + fourth + first + second

		stack.append(merged_string)

	return 'x' + stack[2+1] + stack[3+1] + stack[0+1] + stack[1+1]


def parse_input():
    input = sys.stdin.readline

    # Number of test cases (C ≤ 50)
    C = int(input().strip())
    quadtrees = []

    # Each of the next C lines contains a quadtree-encoded string
    for _ in range(C):
        s = input().strip()
        quadtrees.append(s)

    return C, quadtrees


if __name__ == "__main__":
	quadtree()
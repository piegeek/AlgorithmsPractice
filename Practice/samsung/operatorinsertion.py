import sys
import copy

def operatorinsertion():
    N, A, op_counts = parse_input()
    solve_operatorinsertion(N, A, op_counts)

def solve_operatorinsertion(N, A, op_counts):
	counts = copy.deepcopy(op_counts)

	perms = []
	stack = []
	for i in range(len(counts)):
		if counts[i] > 0:
			stack.append(i)
			counts[i] -= 1
			dfs(i, counts, stack, perms)
			stack.pop(-1)
			counts[i] += 1

	# print(len(perms))
	# print(perms)

	max_val = float('-inf')
	min_val = float('inf')

	for perm in perms:
		operators = perm
		val = calculate_value(A, operators)

		max_val = max(max_val, val)
		min_val = min(min_val, val)

	print(max_val)
	print(min_val)
	return (max_val, min_val)

def calculate_value(A, operators):
	# len(operators) == N-1
	# len(A) == N

	op_pointer = 0

	curr = A[0]

	for i in range(len(operators)):
		next_num = A[i+1]
		# Addition
		if operators[i] == 0:
			curr += next_num
		# Subtraction
		elif operators[i] == 1:
			curr -= next_num
		# Multiplication
		elif operators[i] == 2:
			curr *= next_num
		# Division
		elif operators[i] == 3:
			# Different signs
			if curr * next_num < 0:
				curr = (-1) * (abs(curr) // abs(next_num))
			# Same sign -> Positive
			else:
				curr //= next_num

	return curr


def dfs(idx, counts, stack, perms):
	if all_zero(counts):
		stack_copy = copy.deepcopy(stack)
		perms.append(stack_copy)
		return

	for i in range(len(counts)):
		if counts[i] > 0:
			stack.append(i)
			counts[i] -= 1
			dfs(i, counts, stack, perms)
			stack.pop(-1)
			counts[i] += 1
	

def all_zero(counts):
	for i in range(len(counts)):
		if counts[i] > 0:
			return False
	
	return True

def parse_input():
    input = sys.stdin.readline

    N = int(input().strip())
    A = list(map(int, input().split()))
    op_counts = list(map(int, input().split()))  # [+ , - , * , //]

    return N, A, op_counts


# example usage
if __name__ == "__main__":
	operatorinsertion()
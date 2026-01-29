import sys
import math

def dragon():
    c, test_cases = parse_input()
    for n, p, l in test_cases:
        print(solve_dragon(n, p, l))

def solve_dragon(n, p, l):
	# Brute force - takes too long for large inputs; e.g.: n = 42
	# nth_gen_str = get_nth_gen_str(n)

	# return nth_gen_str[p-1:p-1+l]

	# Mathematical approach
	# if n == 0: return 'FX'
	# if n == 1: return 'FX+YF'[p-1:p-1+l]

	# str_stack = []
	# for i in range(p-1, p+l):
	# 	letter = get_appropriate_letter(i)
	# 	if letter != None:
	# 		str_stack.append(letter)

	# if len(str_stack) == 0: return ''
	# else: return ''.join(str_stack)

	# Optimized brute force approach: Still too slow
	g_n = 'FX'
	gen = 0
	while len(g_n) <= p + l and gen < n:
		g_n = generate_dragon(g_n)
		# print(len(g_n))
		# print(p)
		gen += 1

	if gen == n:
		return g_n[p-1:p-1+l]

	for generation in range(gen, n):
		g_n = generate_dragon(g_n[:p])

	return g_n[p-1:p-1+l]

	
def generate_dragon(string):
	rules_x = 'X+YF'
	rules_y = 'FX-Y'

	stack = []

	for char in string:
		if char == 'X':
			stack.append(rules_x)
		elif char == 'Y':
			stack.append(rules_y)
		else:
			stack.append(char)

	return ''.join(stack)


def get_nth_gen_str(n):
	if n == 0: return 'FX'

	rules_x = 'X+YF'
	rules_y = 'FX-Y'

	n_minus_1_th_gen_str = get_nth_gen_str(n-1)

	stack = []

	for char in n_minus_1_th_gen_str:
		if char == 'X':
			stack.append(rules_x)
		elif char == 'Y':
			stack.append(rules_y)
		else:
			stack.append(char)

	return ''.join(stack)

def get_window(window_size, n):
	if n <= 1: return 'FX+YF'

	rules_x = 'X+YF'
	rules_y = 'FX-Y'

	n_min_1_case = get_window(window_size, n-1)
	# print(n_min_1_case)
	
	stack = []

	for char in n_min_1_case:
		if char == 'X':
			stack.append(rules_x)
		elif char == 'Y':
			stack.append(rules_y)
		else:
			stack.append(char)

	return ''.join(stack[-1-window_size:])

def get_last_idx(char, n, window):
	dragon_length = 2 + 3 * ((2 ** n) - 1)

	ret = -1
	
	first_y_from_back 	  = window[::-1].index('Y')
	first_x_from_back 	  = window[::-1].index('X')
	first_f_from_back 	  = window[::-1].index('F')
	first_plus_from_back  = window[::-1].index('+')
	first_minus_from_back = window[::-1].index('-')

	if char == 'X':

		ret = max(
			(dragon_length - 1) - first_y_from_back + 1,
			(dragon_length - 1) - first_x_from_back
		)

	elif char == 'Y':
		ret = max(
			(dragon_length - 1) - first_y_from_back + 3,
			(dragon_length - 1) - first_x_from_back + 2
		)

	elif char == 'F':
		ret = (dragon_length - 1) - first_f_from_back

	elif char == '+':
		ret = (dragon_length - 1) - first_plus_from_back

	elif char == '-':
		ret = (dragon_length - 1) - first_minus_from_back 

	return ret

def get_appropriate_letter(i):
	# dragon_length = 2 + 3 * ((2 ** n) - 1)
	interval = int(math.log2(((i - 2) / 3) + 1)) + 1

	print(interval)

	window_size = 5
	window = get_window(window_size, interval)

	last_x_idx = get_last_idx('X', interval, window)
	last_y_idx = get_last_idx('Y', interval, window)
	last_f_idx = get_last_idx('F', interval, window)
	last_plus_idx = get_last_idx('+', interval, window)
	last_minus_idx = get_last_idx('-', interval, window)

	if i == last_x_idx:
		return 'X'
	elif i == last_y_idx:
		return 'Y'
	elif i == last_f_idx:
		return 'F'
	elif i == last_plus_idx:
		return '+'
	elif i == last_minus_idx:
		return '-'
	

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (c ≤ 50)
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Dragon curve generation n, position p, length l
        n, p, l = map(int, input().split())
        test_cases.append((n, p, l))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	dragon()
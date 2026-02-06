import sys
import copy
import heapq

def twodarrayoperations():
    r, c, k, A = parse_input()
    solve_twodarrayoperations(r, c, k, A)

# WE DON'T COUNT ZEROS!!
def solve_twodarrayoperations(r, c, k, A):
	ret = -1

	mat = copy.deepcopy(A)

	queue = []

	matrix = mat
		
	heapq.heappush(queue, [0, matrix])

	while len(queue) > 0:
		t, mat = heapq.heappop(queue)

		mat = mat[:100][:100]

		if t > 100:
			break

		if mat[r][c] == k:
			ret = t
			break

		if len(mat) >= len(mat[0]):
			matrix = r_operation(mat)
		else:
			matrix = c_operation(mat)

		heapq.heappush(queue, [t+1, matrix])

	print(ret)
	return ret


def r_operation(mat):
	original_row_len = len(mat[0])

	matrix = copy.deepcopy(mat)

	for i in range(len(matrix)):
		row = matrix[i]

		count_dict = {}

		# WE DON'T COUNT ZEROS!!
		for x in row:
			if x != 0:
				count_dict[str(x)] = 0

		for x in row:
			if x != 0:
				count_dict[str(x)] += 1

		sorted_list = [ (int(x), count_dict[x]) for x in count_dict ]
		sorted_list = sorted(sorted_list, key=lambda x : x[0])
		sorted_list = sorted(sorted_list, key=lambda x : x[1])

		new_row = []

		for num, count in sorted_list:
			new_row.append(num)
			new_row.append(count)

		matrix[i] = new_row

	longest_row_len = max([ len(row) for row in matrix ])
	longest_row_len = max(longest_row_len, original_row_len)

	for i in range(len(matrix)):
		for pad in range(len(matrix[i]), longest_row_len):
			matrix[i].append(0)

	return matrix

def c_operation(mat):
	original_col_len = len(mat)

	matrix = copy.deepcopy(mat)

	new_cols = []

	for j in range(len(matrix[0])):
		col = [ matrix[i][j] for i in range(len(matrix)) ]

		count_dict = {}

		for x in col:
			if x != 0:
				count_dict[str(x)] = 0

		for x in col:
			if x != 0:
				count_dict[str(x)] += 1

		sorted_list = [ (int(x), count_dict[x]) for x in count_dict ]
		sorted_list = sorted(sorted_list, key=lambda x : x[0])
		sorted_list = sorted(sorted_list, key=lambda x : x[1])

		new_col = []

		for num, count in sorted_list:
			new_col.append(num)
			new_col.append(count)

		new_cols.append(new_col)

	longest_col_len = max([ len(new_col) for new_col in new_cols ])
	longest_col_len = max(longest_col_len, original_col_len)

	for new_col in new_cols:
		for pad in range(len(new_col), longest_col_len):
			new_col.append(0)

	for pad in range(len(matrix), longest_col_len):
		matrix.append([0 for _ in range(len(matrix[0]))])

	for j in range(len(new_cols)):
		for i in range(len(new_cols[j])):
				matrix[i][j] = new_cols[j][i]

	return matrix


def parse_input():
    input = sys.stdin.readline

    r, c, k = map(int, input().split())

    A = []
    for _ in range(3):
        A.append(list(map(int, input().split())))

    return r-1, c-1, k, A


# example usage
if __name__ == "__main__":
	twodarrayoperations()
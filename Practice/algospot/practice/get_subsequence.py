def get_subsequence(arr):
	# Base case
	if len(arr) == 0:
		return [[]]

	subseq = [[]]

	for i in range(len(arr)):
		sub = get_subsequence(arr[i+1:])

		for s in sub:
			subseq.append([arr[i]] + s)

	return subseq



if __name__ == '__main__':
	sequence = input().strip()
	arr = list(map(int, sequence.split(' ')))
	subseq = get_subsequence(arr)

	print(len(subseq))

	
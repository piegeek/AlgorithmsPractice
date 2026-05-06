

# n, k = 3, 3
# array = [1, 2, 3]

def combinations_with_replacement(array, k):
	# Base cases
	# k = 0
	# if k == 0: return []
	# if len(array) == 0

	if len(array) == 1:
		pass
		# When k == 0 or not

	# one variable can arrive at base case first (independent two variables)

	# Base case of a, base case of b -> 2
	# 2 x 2 -> 4

	# Solve with two nested ifs.

	combs = []

	# Number of last can be between 0, k
	for i in range(0, k+1):
		possible = combinations_with_replacement(array[:-1], k - i)

		for p in possible:
			for j in range(i):
				p.append(array[-1])

		combs.append(possible)

	return combs
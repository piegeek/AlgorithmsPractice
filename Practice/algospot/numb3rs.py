import sys
import heapq

def numb3rs():
    c, test_cases = parse_input()
    for n, d, p, adj_matrix, t, q in test_cases:
        print(solve_numb3rs(n, d, p, adj_matrix, t, q))

# Check correctness -> probably right; probability of path calculated, added only at leaf
def solve_numb3rs(n, d, p, adj_matrix, t, q):
	ret = [0 for town in q]
	town_count = 0

	day = 1

	queue = []

	neighbors = get_neighbors(p, adj_matrix)

	probability = 1 * (1 / len(neighbors))

	for neighbor in neighbors:
		heapq.heappush(queue, [probability, neighbor, day])

	while len(queue) > 0:
		prob, town, day = heapq.heappop(queue)

		if day == d:
			if town in q:
				ret[q.index(town)] += prob
				town_count += 1

				# if town_count == t:
				# 	break
		
			continue

		neighbors = get_neighbors(town, adj_matrix)

		probability = prob * (1 / len(neighbors))

		for neighbor in neighbors:
			heapq.heappush(queue, [probability, neighbor, day+1])

	return ret

def get_neighbors(town, adj_matrix):
	return [i for i in range(len(adj_matrix[town])) if adj_matrix[town][i] == 1]

def parse_input():
    input = sys.stdin.readline

    # Number of test cases (1 ≤ c ≤ 50)
    c = int(input().strip())
    test_cases = []

    for _ in range(c):
        # Number of villages n, days d, prison village p
        n, d, p = map(int, input().split())

        # Adjacency matrix A (n x n)
        A = []
        for _ in range(n):
            row = list(map(int, input().split()))
            assert len(row) == n
            A.append(row)

        # Number of query villages
        t = int(input().strip())

        # Query village indices
        q = list(map(int, input().split()))
        assert len(q) == t

        test_cases.append((n, d, p, A, t, q))

    return c, test_cases


# Example usage
if __name__ == "__main__":
	numb3rs()
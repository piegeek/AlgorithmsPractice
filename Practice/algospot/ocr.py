import sys
import heapq

def ocr():
    m, q, words, B, T, M, queries = parse_input()

    solve_ocr(m, q, words, B, T, M, queries)
    
def solve_ocr(m, q, words, B, T, M, queries):
    for n, sentence in queries:
        sol_bfs(m, q, words, B, T, M, n, sentence)

def sol_bfs(m, q, words, B, T, M, n, sentence):
	queue = []

	ret = []

	step = 1

	for i in range(len(words)):
		word = words[i]

		prob = B[i]

		if prob > 0:
			heapq.heappush(queue, (prob, [step, [word]]))

	while len(queue) > 0:
		prob, [step, curr_words] = heapq.heappop(queue)

		if step == n:
			ret.append([prob, curr_words])
			continue

		next_word = sentence[step]

		prev_word = curr_words[-1]

		# Next word is correct
		correct_prob = M[words.index(next_word)][words.index(next_word)]
		next_prob = T[words.index(prev_word)][words.index(next_word)]

		heapq.heappush(queue, (prob * correct_prob * next_prob, [step+1, curr_words + [next_word]]))

		# Next word is incorrect
		incorrect_prob = 1 - correct_prob

		for i in range(len(words)):
			if words[i] != next_word:
				next_prob = T[words.index(prev_word)][i]

				heapq.heappush(queue, (prob * incorrect_prob * next_prob, [step+1, curr_words + [words[i]]]))

	ret = sorted(ret, key = lambda x : x[0])
	print(' '.join(ret[-1][1]))
	# print(ret[-1])
	

def parse_input():
    input = sys.stdin.readline

    # Number of words and number of queries
    m, q = map(int, input().split())

    # List of words
    words = input().split()
    assert len(words) == m

    # Initial word probabilities B
    B = list(map(float, input().split()))
    assert len(B) == m

    # Transition matrix T (m x m)
    T = []
    for _ in range(m):
        row = list(map(float, input().split()))
        assert len(row) == m
        T.append(row)

    # Misclassification matrix M (m x m)
    M = []
    for _ in range(m):
        row = list(map(float, input().split()))
        assert len(row) == m
        M.append(row)

    # Classified sentences
    queries = []
    for _ in range(q):
        parts = input().split()
        n = int(parts[0])
        sentence = parts[1:]
        assert len(sentence) == n
        queries.append((n, sentence))

    return m, q, words, B, T, M, queries


# Example usage
if __name__ == "__main__":
	ocr()

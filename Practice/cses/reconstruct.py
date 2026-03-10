# Reconstruct
# 0. Base case - [[]] or []
# 1. Set current_val
# 2. Compare current_val to next step
# 3. suffixes = reconstruct(...)
# 4. When appending answers be mindful of the order format of answer
# 5. Be aware of typos  

# Greedy - garden.py
def reconstruct(idx, start, end, N, flowers, empty):
    if idx == N:
        if end >= 11.30 and start <= 3.01:
            return [[]]
        # For this case we returned INF in dp() here we return []
        else:
            return []

    current_val = dp(idx, start, end, N, flowers, empty)
    
    answers = []

    if current_val == dp(idx + 1, start, end, N, flowers, empty):
        # Should include answer for skip except dont add flowers[idx] into the answer
        suffixes = reconstruct(idx + 1, start, end, N, flowers, empty)
        for suf in suffixes:
            answers.append(suf)

    # Take idx - Empty
    if empty == True:
        start = min(start, flowers[idx][0])
        end = max(end, flowers[idx][1])
        if current_val == 1 + dp(idx + 1, start, end, N, flowers, False):
            suffixes = reconstruct(idx + 1, start, end, N, flowers, False)
            # Put [flowers[idx]] first
            for suf in suffixes:
                answers.append([flowers[idx]] + suf)
            
            return answers
    
    # Take idx
    # Feasibility check
    # Greedy key - choose max end
    if flowers[idx][0] <= end:
        # Merge intervals
        start = min(start, flowers[idx][0])
        end = max(end, flowers[idx][1])
        if current_val == 1 + dp(idx + 1, start, end, N, flowers, False):
            suffixes = reconstruct(idx + 1, start, end, N, flowers, False)
            # Put [flowers[idx]] first
            for suf in suffixes:
                answers.append([flowers[idx]] + suf)

    return answers

# Greedy - library.py
def reconstruct(visited, last, take, N, M, positions, cache):
    if visited == ((1 << N) - 1):
        return [[]]

    current_val = dp(visited, last, take, N, M, positions, cache)

    answers = []

    for i in range(N):
        if (visited & (1 << i)) == 0:
            # Empty
            if take == 0:
                next_take = min(M, N - bin(visited).count('1'))
                visited |= (1 << i)
                if current_val == abs(positions[last] - 0) + abs(0 - positions[i]) + dp(visited, i, next_take - 1, N, M, positions, cache):
                    suffixes = reconstruct(visited, i, next_take - 1, N, M, positions, cache)
                    for suf in suffixes:
                        answers.append([0, positions[i]] + suf)
                visited &= ~(1 << i)
            else:
                if take < M:
                    # Fill and continue
                    next_take = min(M, N - bin(visited).count('1'))
                    visited |= (1 << i)
                    if current_val == abs(positions[last] - 0) + abs(0 - positions[i]) + dp(visited, i, next_take - 1, N, M, positions, cache):
                        suffixes = reconstruct(visited, i, next_take - 1, N, M, positions, cache)
                        for suf in suffixes:
                            answers.append([0, positions[i]] + suf)
                    visited &= ~(1 << i)
    
                # Continue
                visited |= (1 << i)
                if current_val == abs(positions[last] - positions[i]) + dp(visited, i, take - 1, N, M, positions, cache):
                    suffixes = reconstruct(visited, i, take - 1, N, M, positions, cache)
                    for suf in suffixes:
                        answers.append([positions[i]] + suf)
                visited &= ~(1 << i)

    return answers

# CSES - longestcommonsubsequence.py
def reconstruct(i, j, n, m, a, b, cache, solution):
    if i == n or j == m:
        return

    current_val = dp(i, j, n, m, a, b, cache)

    for idx_a in range(i, n):
        for idx_b in range(j, m):
            if a[idx_a] == b[idx_b]:
                next_val = dp(idx_a + 1, idx_b + 1, n, m, a, b, cache)
                if current_val == 1 + next_val:
                    solution.append(a[idx_a])
                    reconstruct(idx_a + 1, idx_b + 1, n, m, a, b, cache, solution)
                    return

def reconstruct_all(i, j, n, m, a, b, cache):
    if i == n or j == m:
        return [[]]

    current_val = dp(i, j, n, m, a, b, cache)
    results = []

    for idx_a in range(i, n):
        for idx_b in range(j, m):
            if a[idx_a] == b[idx_b]:
                next_val = dp(idx_a + 1, idx_b + 1, n, m, a, b, cache)

                if current_val == 1 + next_val:
                    suffixes = reconstruct_all(idx_a + 1, idx_b + 1, n, m, a, b, cache)
                    for suf in suffixes:
                        results.append([a[idx_a]] + suf)

    return results

# CSES - twosets2.py
def reconstruct(idx, visited, n, cache):
    if idx == n:
        visited_sum = 0
        for i in range(n):
            # INCORRECT !!!
            # if (visited & (1 << i)) == 1:
            # CORRECT !!!
            if (visited & (1 << i)):
                visited_sum += (i + 1)
        if visited_sum == ((n * (n + 1)) / 2) * (1 / 2):
            return [[]]
        else:
            return []

    answers = []

    if dp(idx + 1, visited, n, cache) > 0:
        suffixes = reconstruct(idx + 1, visited, n, cache)
        for suf in suffixes:
            answers.append(suf)
    if dp(idx + 1, visited | (1 << idx), n, cache) > 0:
        suffixes = reconstruct(idx + 1, visited | (1 << idx), n, cache)
        for suf in suffixes:
            answers.append([idx+1] + suf)

    return answers
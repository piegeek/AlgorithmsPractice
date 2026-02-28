# BOJ 1461
import sys

INF = 10 ** 9

def library():
    N, M, positions = parse_input()
    solve_library(N, M, positions)

# Permutation - exploration dp, Order: O, Duplicates: X
def solve_library(N, M, positions):
    ret = INF
    visited = 0
    take = M

    cache = {}

    # for i in range(N):
    #     visited |= (1 << i)
    #     ret = min(ret, abs(0 - positions[i]) + dp(visited, i, take-1, N, M, positions, cache))
    #     answers = reconstruct(visited, i, take - 1, N, M, positions, cache)
    #     print(answers)
    #     visited &= ~(1 << i)

    # print(ret)
    # return ret

    ret = greedy(N, M, positions)
    print(ret)
    return ret

def greedy(N, M, positions):
    visited = 0
    curr = 0
    take = M

    count = 0

    while visited != ((1 << N) - 1):
        # Event - Ran out of books
        if take == 0:
            count += abs(curr - 0)
            curr = 0
            take = min(M, N - bin(visited).count('1'))
            continue

        abs_positions = [(abs(curr - positions[i]), i) for i in range(N) if (visited & (1 << i)) == 0 ]

        abs_positions = sorted(abs_positions, key=lambda x : x[0])

        next_idx = abs_positions[0][1]

        count += abs(curr - positions[next_idx])

        visited |= (1 << next_idx)
        take -= 1
        curr = positions[next_idx]

    return count

# O(2^N * N * M)
def dp(visited, last, take, N, M, positions, cache):
    if visited == ((1 << N) - 1):
        return 0

    if (visited, last, take) in cache:
        return cache[(visited, last, take)]

    ret = INF

    for i in range(N):
        if (visited & (1 << i)) == 0:
            # Empty
            if take == 0:
                # print(f'take == 0, visited: {bin(visited)}')
                next_take = min(M, N - bin(visited).count('1'))
                visited |= (1 << i)
                ret = min(ret, abs(positions[last] - 0) + abs(0 - positions[i]) + dp(visited, i, next_take - 1, N, M, positions, cache))
                visited &= ~(1 << i)
            else:
                if take < M:
                    # Fill and continue
                    next_take = min(M, N - bin(visited).count('1'))
                    visited |= (1 << i)
                    ret = min(ret, abs(positions[last] - 0) + abs(0 - positions[i]) + dp(visited, i, next_take - 1, N, M, positions, cache))
                    visited &= ~(1 << i)
    
                # Continue
                visited |= (1 << i)
                ret = min(ret, abs(positions[last] - positions[i]) + dp(visited, i, take - 1, N, M, positions, cache))
                visited &= ~(1 << i)

    cache[(visited, last, take)] = ret
    return ret

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


def parse_input():
    input = sys.stdin.readline  # fast input (safe even if small constraints)
    
    N, M = map(int, input().split())
    positions = list(map(int, input().split()))
    
    return N, M, positions


# Example usage
if __name__ == "__main__":
    library()
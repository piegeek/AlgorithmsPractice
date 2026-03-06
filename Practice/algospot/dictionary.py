import sys
import copy

# 별표

ERROR_MESSAGE = 'INVALID HYPOTHESIS'

def dictionary():
    test_cases = parse_input()

    for i, words in enumerate(test_cases, 1):
        solve_dictionary(words)

def solve_dictionary(words):
    order = [ chr(x) for x in range(97, 97 + 26 ) ]
    visited = [ [ False for _ in range(26) ] for _ in range(26) ]
    
    indices = combinations(words, 2)

    for idx_pair in indices:
        no_contradiction = manipulate_order(idx_pair, order, visited, words)

        if no_contradiction == False:
            print(ERROR_MESSAGE)
            return

    ret = ''.join(order)
    print(ret)
    return ret

def manipulate_order(idx_pair, order, visited, words):
    i, j = idx_pair
    word_a = words[i]
    word_b = words[j]

    for k in range(min(len(word_a), len(word_b))):
        if word_a[k] != word_b[k]:
            # A comes first
            before_letter = word_a[k]
            after_letter = word_b[k]

            before_idx = order.index(before_letter)
            after_idx = order.index(after_letter)

            if before_idx > after_idx:
                # Contradiction
                if visited[before_idx][after_idx] == True:
                    print(order[before_idx])
                    print(order[after_idx])
                    return False

                order[before_idx], order[after_idx] = order[after_idx], order[before_idx]
                visited[before_idx][after_idx] = True
                visited[after_idx][before_idx] = True

            break

    return True

def combinations(arr, k):
    stack = []  
    combs = []
    comb_dp(0, 0, stack, combs, arr, k)
    return combs

def comb_dp(idx, chosen, stack, combs, arr, k):
    if len(stack) == k:
        stack_copy = copy.deepcopy(stack)
        combs.append(stack_copy)
        # RETURN HERE IMPORTANT!!! - PREVENTS DUPLICATES
        return

    # Skip
    if len(arr) - 1 - idx >= k - chosen:
        comb_dp(idx+1, chosen, stack, combs, arr, k)

    # Take
    if chosen + 1 <= k:
        stack.append(idx)
        comb_dp(idx+1, chosen+1, stack, combs, arr, k)
        stack.pop(-1)


# def comb_dp_to_fix(idx, chosen, arr, k):
#     if idx == len(arr):
#         return [[]]

#     if chosen == k:
#         return [[idx]]

#     answers = []

#     # Skip
#     if len(arr) - 1 - idx >= k - chosen:
#         suffixes = comb_dp(idx+1, chosen, arr, k)
#         for suf in suffixes:
#             answers.append(suf)

#     # Take
#     if chosen + 1 <= k:
#         suffixes = comb_dp(idx+1, chosen+1, arr, k)
#         for suf in suffixes:
#             answers.append([idx] + suf)

#     return answers

def parse_input():
    input = sys.stdin.readline
    
    C = int(input().strip())
    test_cases = []

    for _ in range(C):
        N = int(input().strip())
        words = [input().strip() for _ in range(N)]
        test_cases.append(words)

    return test_cases


# Example usage
if __name__ == "__main__":
    dictionary()
import copy

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        S = []
        n = len(s)

        for i in range(n):
            prev_S = copy.deepcopy(S)
            S = [s[i]]

            for j in range(i+1, n):
                if s[j] not in S:
                    S.append(s[j])

                else:
                    idx = S.index(s[j])
                    # Yes inside
                    yes_inside = ''.join(S)

                    # No inside
                    no_inside = ''.join(S[:idx] + S[idx+1:] + [s[j]])

                    if no_inside < yes_inside:
                        S.pop(idx)
                        S.append(s[j])

            if len(prev_S) > 0:
                if (''.join(S) >= ''.join(prev_S) and all_used_once(prev_S, s)) or (all_used_once(prev_S, s) and not all_used_once(S, s)):
                    # print(prev_S)
                    S = prev_S

            print(S)

        return ''.join(S)
        

def all_used_once(prev_S, s):
    letters = list(set([x for x in s]))

    letters_count = [0 for _ in range(len(letters))]

    for i in range(len(prev_S)):
        letters_count[letters.index(prev_S[i])] += 1

    # print(letters_count)

    for i in range(len(letters_count)):
        if letters_count[i] != 1:
            return False

    return True

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        S = []
        n = len(s)

        last = {c: i for i, c in enumerate(s)}
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue

            # 1. Pop while Lexicographically better choice
            # 2. Pop while Can add letter back later
            while len(S) > 0 and c < S[-1] and last[S[-1]] > i:
                seen.remove(S.pop())

            S.append(c)
            seen.add(c)

        return ''.join(S)
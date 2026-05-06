class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack = []

        ret = dp(0, '', s, stack)

        ans = reconstruct(0, '', s, [])

        ret = []

        for i in range(len(ans[0])-1):
            ret.append(ans[0][i+1] - ans[0][i])

        ret.append(len(s) - ans[0][-1])

        return ret

def dp(idx, last, s, stack):
    if idx == len(s):
        return len(stack)

    ret = 0

    if len(stack) == 0:
        last = s[0:idx]
    else:
        last = s[stack[-1]:idx]

    # Take idx
    if last == '' or len([x for x in last if x in s[idx:]]) == 0:
        stack.append(idx)
        ret = dp(idx+1, last, s, stack)
        stack.pop(-1)

    # Skip idx
    ret = max(ret, dp(idx+1, last, s, stack))

    return ret

# DP frontier collapses into 1; Greedy Algorithm
def reconstruct(idx, last, s, stack):
    if idx == len(s):
        return [[]]

    comp = dp(idx, last, s, stack)

    ans = []

    if len(stack) == 0:
        last = s[0:idx]
    else:
        last = s[stack[-1]:idx]

    # Take idx
    if last == '' or len([x for x in last if x in s[idx:]]) == 0:
        stack.append(idx)
        if comp == dp(idx+1, last, s, stack):
            for res in reconstruct(idx+1, last, s, stack):
                ans.append([idx] + res)
        stack.pop(-1)

    # Skip idx
    if comp == dp(idx+1, last, s, stack):
        for res in reconstruct(idx+1, last, s, stack):
            ans.append(res)

    return ans

# In a lot a greedy problems such as this one, I feel like tracking the entirety of the
# prefix in unnecessary. Instead it is okay to just check the last state (Markov Property)
class Solution2:
    def partitionLabels(self, s: str) -> List[int]:
        S = []

        idx = 0

        for i in range(len(s)):
            word = s[idx:i]

            if len([x for x in word if x in s[i:]]) == 0:
                S.append(i)
                idx = i

        ret = []

        for i in range(len(S) - 1):
            ret.append(S[i+1] - S[i])

        ret.append(len(s) - S[-1])

        return ret


    


        
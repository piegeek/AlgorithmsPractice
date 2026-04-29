class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        S = []

        g = sorted(g)
        s = sorted(s)

        visited_g = [False for _ in range(len(g))]
        visited_s = [False for _ in range(len(s))]

        for j in range(len(s)):
            for i in range(len(g)):
                if s[j] >= g[i] and not visited_g[i] and not visited_s[j]:
                    S.append(s[j])
                    visited_g[i] = True
                    visited_s[j] = True
                    break

        return len(S)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        S = []

        g = sorted(g)
        s = sorted(s)

        g_pointer = 0
        s_pointer = 0

        while s_pointer < len(s) and g_pointer < len(g):
            if s[s_pointer] >= g[g_pointer]:
                S.append(s[s_pointer])
                s_pointer += 1
                g_pointer += 1

            else:
                s_pointer += 1

        return len(S)

        

        
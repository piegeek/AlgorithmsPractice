import sys

sys.set_int_max_str_digits(10 ** 6)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        S = []

        n = len(num)
        pop_count = 0

        for e in num:
            while len(S) > 0 and int(e) < S[-1] and pop_count < k:
                S.pop(-1)
                pop_count += 1

            S.append(int(e))

        while pop_count < k:
            S.pop(-1)
            pop_count += 1

        if n - k == 0:
            return '0'

        return str(int(''.join(list(map(str, S)))))
        
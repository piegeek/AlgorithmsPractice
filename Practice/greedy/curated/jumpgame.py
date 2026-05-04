class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        cache = {}

        ret = dp(0, nums, n, cache)

        return ret

def dp(idx, nums, n, cache):
    if idx >= n - 1:
        return True

    if idx in cache:
        return cache[idx]

    ret = False

    for val in range(1, nums[idx] + 1):
        ret = dp(idx + val, nums, n, cache) or ret

    cache[idx] = ret
    return ret

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        idx = 0

        while idx < n - 1:
            print(idx)

            if nums[idx] == 0:
                return False

            step_size = nums[idx]

            max_next = 1 + nums[idx + 1]
            max_next_idx = 1

            for s in range(1, step_size + 1):
                if idx + s > n - 1:
                    return True
                elif s + nums[idx + s] >= max_next or idx + s == n - 1:
                    max_next = s + nums[idx + s]
                    max_next_idx = s

            idx += max_next_idx

        return True


        
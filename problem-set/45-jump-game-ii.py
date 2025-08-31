from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        memoize = [0] * len(nums)
        i = 1
        while i < len(nums):
            j = 0
            min_steps = len(nums)
            while j < i:
                if j + nums[j] >= i:
                    steps = memoize[j] + 1
                    if steps < min_steps:
                        min_steps = steps
                j += 1
            memoize[i] = min_steps
            i += 1
        return memoize[-1]

s = Solution()
print("solution ", s.jump([1,2,1,1,1]))
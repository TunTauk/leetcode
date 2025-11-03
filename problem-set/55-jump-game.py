from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = nums[i] + 1
        while i < len(nums) and i < j:
            j = max(i + nums[i] + 1, j)
            print(i, j)
            i += 1
        if i == len(nums):
            return True
        return False


s = Solution()
print(s.canJump([2,0]))

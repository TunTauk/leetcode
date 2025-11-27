from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        dp = [0, 0, 0]
        dp[nums[0] % 3] = nums[0]
        for i in range(1, n):
            num = nums[i]
            state = num % 3
            old = dp[:]
            new = dp[:]
            for prev in range(3):
                curr = (prev + state) % 3
                candidate = 0
                if old[prev] != 0:
                    candidate = old[prev] + num
                else:
                    candidate = num if prev == 0 else 0
                new[curr] = max(new[curr], candidate)
            dp = new
        return dp[0]


s = Solution()
print(s.maxSumDivThree([2,6,2,2,7]))


[[0, 6, 0, 0, 0], [0, 0, 0, 0, 0], [8, 8, 0, 0, 0]]

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        total = 0
        for num in nums:
            total += num
            prefix_sum.append(total)
        l = len(nums)
        maxi = prefix_sum[k-1]
        for step in range(k, l + 1, k):
            for index in range(len(nums) - step + 1):
                pad = prefix_sum[index - 1] if index != 0 else 0
                maxi = max(prefix_sum[step + index - 1] - pad, maxi)
        return maxi
        

s = Solution()
print(s.maxSubarraySum(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=3))
print(s.maxSubarraySum(nums=[1, 2], k=1))
print(s.maxSubarraySum([-1, -2, -3, -4, -5], k=4))
print(s.maxSubarraySum(nums=[-5, 1, 2, -3, 4], k=2))
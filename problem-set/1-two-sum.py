class Solution(object):
    def twoSum(self, nums, target):
        for i, x in enumerate(nums):
          for j, y in enumerate(nums):
            if i != j and x+y == target:
              return [i, j]
          
          
s = Solution()
print("solution ", s.twoSum([1,2,3], 5))
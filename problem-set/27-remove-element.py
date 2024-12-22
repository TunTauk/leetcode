class Solution(object):
    def removeElement(self, nums, val):
      i = 0
      j = 0
      while i < len(nums):
        if nums[i] != val:
          nums[j] = nums[i]
          j += 1
        i += 1
      return j
    
    
s = Solution()
print("solution ", s.removeElement([0,0,1,2,2,3,4,5,5], 0))
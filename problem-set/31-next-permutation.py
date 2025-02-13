from typing import List

class Solution:
  
  def isDesendingOrder(self, nums: List[int], i: int) -> bool:
    while i < len(nums) - 1:
      if nums[i] < nums[i + 1]:
        return False
      i += 1
    return True
  
  def reverse(self, nums: List[int], start: int, end: int) -> int:
    while start < end:
      nums[start], nums[end]  = nums[end], nums[start]
      start += 1
      end -= 1
    
  def getSmallestIndex(self, nums: List[int], i: int):
    limit = nums[i]
    smallest = 101
    index = -1
    while i < len(nums) - 1:
      if nums[i + 1] < smallest and nums[i + 1] > limit:
        smallest = nums[i + 1]
        index = i + 1
      i += 1
    return index
  
  def nextPermutation(self, nums: List[int]) -> None:
    nums_len = len(nums)
    i = nums_len - 2
    while i >= 0:
      if self.isDesendingOrder(nums, i):
        i -= 1
      else:
        self.reverse(nums, i + 1, nums_len - 1)
        j = self.getSmallestIndex(nums, i)
        nums[i], nums[j]  = nums[j], nums[i]
        break
    if i == -1:
      self.reverse(nums, 0, nums_len - 1)
    print(nums)
        
    
s = Solution()
print("solution ", s.nextPermutation([1, 3, 2]))
        
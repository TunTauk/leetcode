from typing import List

class Solution:
  
    def binarySearch(self, arr: List[int], low: int, high: int, x: int) -> int:
      if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
          return mid
        elif arr[mid] > x:
          return self.binary_search(arr, low, mid - 1, x)
        else:
          return self.binary_search(arr, mid + 1, high, x)
      else:
        return -1
  
    def search(self, nums: List[int], target: int) -> int:
      i = 0
      while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
          j = self.binarySearch(nums, 0, i, target)
          if j == -1:
            return self.binarySearch(nums, i + 1, len(nums) - 1, target)
          return j
        i += 1
      return self.binarySearch(nums, 0, len(nums) - 1, target)
    
s = Solution()
print("solution ", s.search([4,5,6,7,0,1,2], 0))
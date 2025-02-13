from typing import List


class Solution:
  
  def binarySearch(self, arr: List[int], low: int, high: int, x: int) -> int:
    if high >= low:
      mid = (high + low) // 2
      if arr[mid] == x:
        return mid
      elif arr[mid] > x:
        return self.binarySearch(arr, low, mid - 1, x)
      else:
        return self.binarySearch(arr, mid + 1, high, x)
    else:
      return -1
  
  def getLowerLimit(self, arr: List[int], low: int, high: int, x: int) -> int:
    if high >= low:
      mid = (high + low) // 2
      if arr[mid] == x:
        if mid == 0 or arr[mid -1] != x:
          return mid
        else: 
          return self.getLowerLimit(arr, low, mid - 1, x)
      else:
        return self.getLowerLimit(arr, mid + 1, high, x)
      
  def getUpperLimit(self, arr: List[int], low: int, high: int, x: int) -> int:
    if high >= low:
      mid = (high + low) // 2
      if arr[mid] == x:
        if mid == len(arr) -1 or arr[mid + 1] != x:
          return mid
        else: 
          return self.getUpperLimit(arr, mid + 1, high, x)
      else:
        return self.getUpperLimit(arr, low, mid -1, x)
  
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    i = self.binarySearch(nums, 0, len(nums) -1, target)
    if i == -1: return [-1, -1]
    print(i)
    return [
      self.getLowerLimit(nums, 0, i, target),
      self.getUpperLimit(nums, i, len(nums) -1, target)
    ]
    
    
s = Solution()
print("solution ", s.searchRange([1], 1))
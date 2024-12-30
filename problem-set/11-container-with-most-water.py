from typing import List

class Solution:
  
  def maxArea(self, height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    max_area = 0
    while i < j:
      area = min(height[i], height[j]) * (j - i)
      if area > max_area:
        max_area = area
      if height[i] < height[j]:
        i += 1
      else:
        j -= 1
    return max_area
  
s = Solution()
print("solution",s.maxArea([2,3,4,5,18,17,6]))
from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n = len(nums1)
    m = len(nums2)
    o = int((n+m)/2) + 1
    result_list = [0] * o
    i = 0
    j = 0
    k = 0
    while i < n and j < m and k < o:
      if nums1[i] <= nums2[j]:
        result_list[k] = nums1[i]
        i += 1
      else:
        result_list[k] = nums2[j]
        j += 1
      k += 1
    while i < n and k < o:
      result_list[k] = nums1[i]
      i += 1
      k += 1
    while j < m and k < o:
      result_list[k] = nums2[j]
      j += 1
      k += 1
    if (n+m) % 2 == 0:
      return (result_list[o-1]+ result_list[o-2]) /2
    else:
      return result_list[o-1]
      
    
s = Solution()
print("solution",s.findMedianSortedArrays([1], []))
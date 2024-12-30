from typing import Dict, List, Set

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    one_set: Set[int] = set()
    two_set: Set[int] = set()
    mod_set: Set[int] = set()
    zero = 0
    for num in nums:
      if num == 0:
        zero += 1
      else:
        if -num in one_set:
          mod_set.add(abs(num))
        if num in one_set:
          two_set.add(num)
        one_set.add(num)
    result: List[List[int]] = []
    if zero >= 3:
      result.append([0, 0, 0])
    for v in two_set:
      other = v * -2
      if other in one_set:
        result.append([v, v, other])
    if zero >= 1:
      for v in mod_set:
        result.append([v, -v, 0])
    l = sorted(one_set)
    dict: Dict[int, int] = {}
    for i,v in enumerate(l):
      dict[v] = i
    start = 0
    while start < len(l)-1 and l[start] < 0:
      end = len(l) - 1
      while end > 0 and l[end] > 0:
        val = -(l[start] + l[end])
        third = dict.get(val)
        if third and third > start and third < end:
          result.append([l[start], l[end], val])
        end -= 1
      start += 1
    return result  
    
s = Solution()
print("solution",s.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
    
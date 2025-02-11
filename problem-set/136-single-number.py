from typing import List, Dict

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    count: Dict[int, int] = {}
    for num in nums:
      if count.get(num):
        count[num] += 1
      else:
        count[num] = 1
    for key, value in count.items():
      if count[key] == 1:
        return key
      
s = Solution()
s.singleNumber([1,2,3,4,1])
from typing import List, Dict

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict: Dict[int, int] = {}
    for i, v in enumerate(nums):
      dict[v] = i
    for i, v in enumerate(nums):
      k = dict.get(target-v)
      if k and i != k:
        return [i, k]
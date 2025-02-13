from typing import List, Dict


class Solution:
  
  result: Dict[str, List[List[int]]] = {}
  
  def _combinationSum(self, candidates: List[int], path: List[int], target: int):
    if target == 0:
      path.sort()
      key = ','.join([str(x) for x in path])
      if not self.result.get(key):
        self.result[key] = path
    elif target > 0:
      for val in candidates:
        self._combinationSum(candidates, path + [val], target - val)
    
  
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    self.result = {}
    self._combinationSum(candidates, [], target)
    return list(self.result.values())
    
s = Solution()
print("solution ", s.combinationSum([2,3,5], 8))
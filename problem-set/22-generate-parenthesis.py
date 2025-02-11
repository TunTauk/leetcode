from typing import List

class Solution:
  
  result = set()
  
  def _generateParenthesis(self, brackets: str, open_count: int, close_count: int):
    if open_count == 0:
      i = 0
      while i < close_count:
        brackets += ")"
        i += 1
      self.result.add(brackets)
    else:
      self._generateParenthesis(brackets + "(", open_count - 1, close_count)
      if open_count < close_count:
        self._generateParenthesis(brackets + ")", open_count, close_count - 1)
    
  
  def generateParenthesis(self, n: int) -> List[str]:
    self.result = set()
    self._generateParenthesis("", n, n)
    return list(self.result)
    
    
s = Solution()
print("solution",s.generateParenthesis(1))
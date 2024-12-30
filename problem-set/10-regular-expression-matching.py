

class Solution:  
  
  def _isMatch(self, s: str, p: str, i: int, j: int) -> bool:
    if j == 0:
      return i == 0
    if i == 0:
      return p[j-1] == '*' and self._isMatch(s, p, i, j -2)
    if s[i-1] == p[j-1] or p[j-1] == '.':
      return self._isMatch(s, p, i - 1, j - 1)
    if p[j-1] == '*':
      is_zero_match = self._isMatch(s, p, i, j - 2)
      is_one_match = (s[i-1] == p[j-2] or p[j-2] == '.') and self._isMatch(s, p, i-1, j)
      return is_zero_match or is_one_match
    return False
  
  def isMatch(self, s: str, p: str) -> bool:
    return self._isMatch(s,p, len(s), len(p))
    
      
          
        
    

s = Solution()
print("solution",s.isMatch("aab", ".*.*p*p*pp....*.*....*"))
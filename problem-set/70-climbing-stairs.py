class Solution:
    result = [0] + [1] + [2] + [0]*43
    def climbStairs(self, n: int) -> int:
      result = self.result[n] if self.result[n] != 0 else (self.climbStairs(n-1) + self.climbStairs(n-2))
      self.result[n] = result
      return result
        
s = Solution()
print("solution ", s.climbStairs(45))
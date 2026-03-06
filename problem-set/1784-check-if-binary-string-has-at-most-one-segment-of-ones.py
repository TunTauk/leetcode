class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        foundOther = False
        for c in s:
          if foundOther and c == "1":
            return False
          if c != "1":
            foundOther = True
            
        return True
      
s = Solution()
class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 1
        result = 1
        while n > result:
          result = 2 ** i -1
          i += 1
        return result
      
     
s = Solution()
print("solution ", s.smallestNumber(7))
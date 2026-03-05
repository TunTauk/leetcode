class Solution:
    def minOperations(self, s: str) -> int:
        ch = "1"
        count = 0
        for c in s:
          if c != ch:
            count += 1
          ch = "1" if ch == "0" else "0"
        ch = "0"
        sec_count = 0
        for c in s:
          if c != ch:
            sec_count += 1
          ch = "1" if ch == "0" else "0"
        return min(count, sec_count)
        
        
        
s = Solution()
print(s.minOperations("0100"))
print(s.minOperations("10"))
print(s.minOperations("1111"))
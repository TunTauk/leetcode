from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lss = 0
        i = 0
        while i <= len(s) - 1:
          j = i
          temp = 0
          dict: Dict[int, bool] = {}
          while j <= len(s) - 1:
            key = ord(s[j])
            if dict.get(key, False):
              break
            temp += 1
            dict[key] = True
            j += 1
          print(lss, temp)
          lss = max(lss, temp)
          i += 1
        return lss
      
s = Solution()
print("solution ",s.lengthOfLongestSubstring(" "))
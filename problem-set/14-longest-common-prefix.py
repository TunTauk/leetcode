

class Solution(object):
    def longestCommonPrefix(self, strs):
      shortest_length = len(strs[0])
      for str in strs:
        if shortest_length > len(str):
          shortest_length = len(str)
        
      i = 0
      lcp = ""
      while i < shortest_length:
        j = 0
        while j < len(strs)-1:
          if strs[j][i] != strs[j+1][i]:
            return lcp
          j += 1
        lcp += strs[0][i]
        i += 1
      return lcp
        
             
s = Solution()
print("solution ", s.romanToInt("III"))
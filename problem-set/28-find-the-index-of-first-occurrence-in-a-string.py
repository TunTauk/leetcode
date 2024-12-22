class Solution(object):
    def strStr(self, haystack, needle):
      i = 0
      while i < len(haystack) - len(needle) + 1:
        if haystack[i:i+len(needle)] == needle:
          return i
        i += 1
      return -1
    
s = Solution()
print("solution ", s.strStr("sadbutsad", "sad"))
class Solution(object):
    def lengthOfLastWord(self, s):
      i = len(s) - 1
      
      while i >= 0:
        if s[i] != ' ':
          break
        i -= 1
      j = i
      while i >= 0:
        if s[i] == ' ':
          return j - i
        i -= 1
      return j - i


s = Solution()
print("solution ", s.lengthOfLastWord("a"))
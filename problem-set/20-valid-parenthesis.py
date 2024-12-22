class Solution(object):
    def isValid(self, s):
      stack = []
      open_set = { "{", "(", "["}
      full_set = { "{}", "()", "[]"}
      for c in s:
        if c in open_set:
          stack.append(c)
        else:
          if len(stack) == 0 or stack.pop() + c not in  full_set:
            return False
      return len(stack) == 0
       
s = Solution()
print("solution ", s.isValid("[]"))
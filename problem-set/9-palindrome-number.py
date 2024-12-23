class Solution(object):
    def isPalindrome(self, x):
      y = str(x)
      start = 0
      end = len(y) - 1
      while start <= end:
        if y[start] != y[end]:
          return False
        start += 1
        end -= 1
      return True
      


s = Solution()
print("solution ",s.isPalindrome(1221))
class Solution:
  def isPalindrome(self, s:str) -> bool:
    start = 0
    end = len(s) - 1
    while start <= end:
      if s[start] != s[end]:
        return False
      start += 1
      end -= 1
    return True
    
  def longestPalindrome(self, s: str) -> str:
    l = len(s)
    max_len = l
    while max_len >= 0:
      i = 0
      while i + max_len - 1 < l:
        sub_s = s[i:i+max_len]
        if self.isPalindrome(sub_s):
          return sub_s
        i += 1
      max_len -= 1
    return ""
  
  def longestPalindrome(self, s: str) -> str:
    l = len(s)
    p_matrix = [[False for _ in range(l)] for _ in range(l)]
    def isPalindrome(start: int, end: int) -> bool:
      if start >= end: return True
      if p_matrix[start][end]:
        return True
      is_palindrome = s[start] == s[end] and isPalindrome(start+1,end-1)
      p_matrix[start][end] = is_palindrome
      return is_palindrome
    max_len = l
    while max_len >= 0:
      i = 0
      while i + max_len - 1 < l:
        if isPalindrome(i,i + max_len-1):
          return s[i:i+max_len]
        i += 1
      max_len -= 1
    return ""
    

s = Solution()
print("solution",s.longestPalindrome("abb"))
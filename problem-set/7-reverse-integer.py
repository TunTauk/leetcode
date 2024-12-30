class Solution:
  def reverse(self, x: int) -> int:
    limit = 214748364
    limit_2 = 7
    ans = 0
    is_negative = True if x < 0 else False
    x = abs(x)
    while x >= 10:
      mod = x % 10
      ans = ans * 10 + mod
      x = int(x/10)
    mod = x % 10
    if ans > limit or (ans == limit and mod > limit_2):
      return 0
    ans = ans * 10 + mod
    return ans * -1 if is_negative else ans
  
s = Solution()
print("solution ",s.reverse(-2147483412))
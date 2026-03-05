class Solution:
  def findKthBit(self, n: int, k: int) -> str:
    def inverted(s: str) -> str:
      new_s = ""
      for c in s:
        new_s += "1" if c == "0" else "0"
      return new_s
    def buildString(s: str, n: int) -> str:
      if n == 1:
        return "0"
      new_s = buildString(s, n-1)
      return new_s + "1" + "".join(reversed(inverted(new_s)))
    result = buildString("", n)
    print(result)
    return result[k-1]
  
s = Solution()
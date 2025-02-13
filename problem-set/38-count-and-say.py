class Solution:

  def countAndSay(self, n: int) -> str:
    result = "1"
    i = 0
    while i < n - 1:
      count = 1
      j = 0
      current = result[j]
      new_result = ""
      while j < len(result) - 1:
        if current != result[j + 1]:
          new_result += str(count) + current
          count = 1
          current = result[j + 1]
        else:
          count += 1
        j += 1
      result = new_result + str(count) + current
      i += 1
    return result
  
s = Solution()
print("solution ", s.countAndSay(4))
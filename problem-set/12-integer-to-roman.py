class Solution:
  def intToRoman(self, num: int) -> str:
    dict = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I")
    ]
    result = ""
    while num > 0:
      v = 0
      s = ""
      for d in dict:
        if num >= d[0]:
          v = d[0]
          s = d[1]
          break
      result += s
      num -= v
    return result
  
  
s = Solution()
print("solution",s.intToRoman(1994))
    
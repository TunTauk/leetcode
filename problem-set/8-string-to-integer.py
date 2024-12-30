class Solution:
  def myAtoi(self, s: str) -> int:
    result = ""
    sign = {"-", "+"}
    digit = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    i = 0
    limit = 12
    found_sign = False
    found_digit = False
    is_leading = True
    while i < len(s) and len(result) < limit:
      if s[i] == " " and not found_digit and not found_sign:
        i += 1
        continue
      if s[i] == "0":
        if not is_leading:
          result += s[i]
        i += 1
        found_digit = True
        continue
      if s[i] in sign and not found_sign and not found_digit:
        found_sign = True
        result += s[i]
        i += 1
        continue
      if s[i] in digit:
        found_digit = True
        is_leading = False
        result += s[i]
        i += 1
        continue
      break
    if not result: return 0
    if result in sign: return 0
    result = int(result)
    if result > 2147483647: return 2147483647
    if result < -2147483648: return -2147483648
    return result

s = Solution()
print("solution",s.myAtoi("  0000000000012345678"))
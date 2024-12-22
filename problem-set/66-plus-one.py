class Solution(object):
    def plusOne(self, digits):
      is_all_nine = True
      i = 0
      while i < len(digits):
        if digits[i] != 9:
          is_all_nine = False
          break
        i += 1
      if is_all_nine:
        return [1] + [0] * len(digits)
      i = len(digits) - 1
      while i >= 0:
        if digits[i] == 9:
          digits[i] = 0
          i -= 1
          continue
        else:
          digits[i] += 1
          break
      return digits

s = Solution()
print("solution ",s.plusOne([1,9,9,9,9,9]))

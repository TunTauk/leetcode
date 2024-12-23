import math 
class Solution(object):
    def mySqrt(self, x):
      x_str = str(x)
      half = math.ceil(len(x_str) / 2) - 1
      start = int("".join((["1"] + ["0"] * half)))
      while start * start <= x:
        start += 1
      return start - 1

    
s = Solution()
print("solution ", s.mySqrt(105))
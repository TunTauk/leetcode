import numpy as np


class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1: return s
    is_down = True
    s_matrix = [['' for _ in range(len(s))] for _ in range(numRows)]
    row = 0
    col = 0
    for c in s:
      s_matrix[row][col] = c
      if is_down:
        row += 1
      if row == numRows:
        is_down = False
        col += 1
        row -= 1
      if not is_down:
        row -= 1
      if row == 0:
        is_down = True
        col += 1
    result = ""
    for i in s_matrix:
      for c in i:
        result += c
    return result
    
    
s = Solution()
print("solution ",s.convert("PAYPALISHIRING", 2))
      
      
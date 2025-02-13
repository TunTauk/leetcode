from typing import List, Set

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValid(digit: str, digits: Set[str]):
      if digit == ".": return True
      if digit in digits:
        digits.remove(digit)
        return True
      return False
    
    def createDigits():
      return {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    
    # valid rows
    i = 0
    while i < 9:
      digits = createDigits()
      j = 0
      while j < 9:
        if not isValid(board[i][j], digits):
          return False
        j += 1
      i +=1
      
    #valid columns
    j = 0
    while j < 9:
      i = 0
      digits = createDigits()
      while i < 9:
        if not isValid(board[i][j], digits):
          return False
        i += 1
      j += 1
      
    #valid blocks
    i = 0
    while i < 3:
      j = 0
      while j < 3:
        k = 0
        digits = createDigits()
        while k < 3:
          l = 0
          while l < 3:
            if not isValid(board[i*3+k][j*3+l], digits):
              return False
            l += 1
          k += 1
        j += 1
      i += 1
    return True
  
s = Solution()
print("solution ", s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
        
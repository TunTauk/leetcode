from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(row : int, col : int, index : int):
          if index == len(word):
            return True
          if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[index]:
            return False
          
          temp = board[row][col]
          board[row][col] = "#"
          
          found = (dfs(row=row + 1, col=col, index=index+1) or 
                   dfs(row=row - 1, col=col, index=index+1) or
                   dfs(row=row, col=col + 1, index=index+1) or
                   dfs(row=row , col=col - 1, index=index+1))
          
          board[row][col] = temp
                    
          return found
        
        found = False
        for row in range(rows):
          for col in range(cols):
            if board[row][col] == word[0]:
              found = dfs(row=row, col=col, index=0)
              if found:
                return True
        return found
        
      
Test = Solution()
print(Test.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))


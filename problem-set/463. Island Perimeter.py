from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
      rows, cols = len(grid), len(grid[0])
      
      def dfs(row : int, col : int):
        if row < 0 or col < 0 or row >= rows or col >= cols:
          return 1
        
        if grid[row][col] == -1:
          return 0
        
        if grid[row][col] == 0:
          return 1
        
        grid[row][col] = -1
        parameter = 0
        
        for r,c in [(-1,0),(1,0),(0,1),(0,-1)]:
          parameter += dfs(row=row + r, col= col + c)
          
        return parameter
      
      for row in range(rows):
        for col in range(cols):
          if grid[row][col] == 1:
            return dfs(row=row, col=col)
    
Test = Solution()
print(Test.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
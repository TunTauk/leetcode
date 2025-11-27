from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        prev_dp = [[0 for _ in range(k)] for _ in range(cols)]
        curr_dp = [[0 for _ in range(k)] for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                num = grid[row][col]
                if row == 0 and col == 0:
                    curr_dp[0][grid[0][0] % k] = 1
                    continue
                for i in range(k):
                    index = (num + i) % k
                    if row != 0 and prev_dp[col][i] != 0:
                        curr_dp[col][index] += prev_dp[col][i]
                    if col != 0 and curr_dp[col - 1][i] != 0:
                        curr_dp[col][index] += curr_dp[col-1][i]
            prev_dp = curr_dp
            curr_dp = [[0 for _ in range(k)] for _ in range(cols)]
        limit = (10**9 + 7)
        return prev_dp[cols - 1][0] % limit


s = Solution()
print(s.numberOfPaths(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3))
print(s.numberOfPaths(grid=[[0, 0]], k=5))
print(s.numberOfPaths(grid=[[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], k=1))

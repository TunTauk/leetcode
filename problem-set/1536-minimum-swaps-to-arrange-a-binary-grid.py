from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vals = [0] * n

        row = 0
        while row < n:
            col = n - 1
            count = 0
            while col >= 0:
                if grid[row][col] == 0:
                    count += 1
                else:
                    vals[row] = count
                    break
                col -= 1
            if col == -1:
                vals[row] = n
            row += 1
        swap_count = 0
        for i in range(n - 1):
            if vals[i] < n - i - 1:
                j = i + 1
                while j < n and vals[j] < n - i - 1:
                    j += 1
                if j == n:
                    return -1
                k = j
                while k > i:
                    vals[k], vals[k - 1] = vals[k - 1], vals[k]
                    k -= 1
                swap_count += j - i

        return swap_count


s = Solution()
print(s.minSwaps(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(s.minSwaps(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))
print(s.minSwaps(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
print(s.minSwaps(grid=[[0, 0], [0, 1]]))
print(
    s.minSwaps(
        grid=[
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0],
        ]
    )
)
print(
    s.minSwaps(
        grid=[
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
        ]
    )
)

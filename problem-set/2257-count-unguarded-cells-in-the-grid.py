from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # m = row and n = col
        col_cells = [[0 for _ in range(n)] for _ in range(m)]
        row_cells = [[0 for _ in range(n)] for _ in range(m)]
        for wall in walls:
            [wall_row, wall_col] = wall
            row_cells[wall_row][wall_col] = 2
            col_cells[wall_row][wall_col] = 2
        for guard in guards:
            [guard_row, guard_col] = guard
            row_cells[guard_row][guard_col] = 1
            col_cells[guard_row][guard_col] = 1
        # guard top
        for guard in guards:
            [guard_row, guard_col] = guard
            row = guard_row - 1
            while (
                row >= 0
                and col_cells[row][guard_col] != 2
                and col_cells[row][guard_col] != 1
            ):
                col_cells[row][guard_col] = 1
                row -= 1

        # guard bottom
        for guard in guards:
            [guard_row, guard_col] = guard
            row = guard_row + 1
            while (
                row < m
                and col_cells[row][guard_col] != 2
                and col_cells[row][guard_col] != 1
            ):
                col_cells[row][guard_col] = 1
                row += 1
        # guard left
        for guard in guards:
            [guard_row, guard_col] = guard
            col = guard_col - 1
            while (
                col >= 0
                and row_cells[guard_row][col] != 2
                and row_cells[guard_row][col] != 1
            ):
                row_cells[guard_row][col] = 1
                col -= 1
        for guard in guards:
            [guard_row, guard_col] = guard
            col = guard_col + 1
            while (
                col < n
                and row_cells[guard_row][col] != 2
                and row_cells[guard_row][col] != 1
            ):
                row_cells[guard_row][col] = 1
                col += 1
        count = 0
        row = 0
        while row < m:
            col = 0
            while col < n:
                if row_cells[row][col] == 0 and col_cells[row][col] == 0:
                    count += 1
                col += 1
            row += 1
        return count


s = Solution()
print(
    s.countUnguarded(
        m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]
    )
)

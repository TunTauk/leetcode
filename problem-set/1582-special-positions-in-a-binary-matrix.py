from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            if sum(mat[row]) != 1:
                continue
            for col in range(cols):
                if mat[row][col] == 1:
                    i = 0
                    for j in range(rows):
                        if mat[j][col] == 0:
                            i += 1
                    if i == rows - 1:
                        count += 1
        return count


test = Solution()
# print(test.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
# print(test.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
# print(test.numSpecial(mat=[[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(
    test.numSpecial(
        mat=[
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)

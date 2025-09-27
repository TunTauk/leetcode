class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        n, m = len(s1), len(s2)
        memo = [[False] * (m + 1) for _ in range(n + 1)]
        memo[0][0] = True

        def getVal(row: int, col: int) -> bool:
            if row == 0 and col == 0: return True
            from_col = (
                col > 0 and memo[row][col - 1] and s2[col - 1] == s3[row + col - 1]
            )
            from_row = (
                row > 0 and memo[row - 1][col] and s1[row - 1] == s3[row + col - 1]
            )
            return from_row or from_col

        for row in range(n + 1):
            for col in range(m + 1):
                memo[row][col] = getVal(row, col)
        return memo[-1][-1]


s = Solution()
print("solution ", s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

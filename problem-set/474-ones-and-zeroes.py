from typing import List, Tuple
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        str_dicts: List[Tuple[int, int]] = []
        strs.sort(key=lambda x: len(x))
        total = m + n
        for str in strs:
            c = Counter(str)
            zero, one = c["0"], c["1"]
            if total >= zero + one:
                str_dicts.append((c["0"], c["1"]))
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for (z, o) in str_dicts:
            for i in range(m, z - 1, -1):
                for j in range(n, o - 1, -1):
                    print(i,j)
                    dp[i][j] = max(dp[i][j], dp[i-z][j-o] + 1)
            print(dp)
        return dp[m][n]
                                                                                     

s = Solution()
print(s.findMaxForm(strs = ["10","0001","111001","1","0"], m = 5, n = 3))
# print(
#     s.findMaxForm(
#         ["0", "1101", "01", "00111", "1", "10010", "0", "0", "00", "1", "11", "0011"],
#         63,
#         36,
#     )
# )

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            return [*range(-1 * int(n / 2), 0), *range(1, int(n / 2) + 1)]
        else:
            return list(range(-1 * int(n / 2), int(n / 2) + 1))


s = Solution()
print(s.sumZero(6))

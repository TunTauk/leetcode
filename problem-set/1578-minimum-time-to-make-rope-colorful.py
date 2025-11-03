from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        i = 0
        while i < len(colors) - 1:
          j = i + 1
          max_time = neededTime[i]
          total = neededTime[i]
          while j < len(colors) and colors[i] == colors[j]:
            max_time = max(max_time, neededTime[j])
            total += neededTime[j]
            j += 1
          i = j
          cost += (total - max_time)
        return cost
      
s = Solution()
print(s.minCost("aaabb", [1, 2, 3, 4, 1]))
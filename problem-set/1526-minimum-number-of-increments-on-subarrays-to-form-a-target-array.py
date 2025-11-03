from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if len(target) == 1:
          return target[0]
        peaks = []
        lowest = []
        i = 0
        while i < len(target) - 1:
          while i < len(target) - 1 and target[i] <= target[i + 1]:
            i += 1
          peaks.append(target[i])
          while i < len(target) - 1 and target[i] >= target[i+ 1]:
            i += 1
          lowest.append(target[i])
        count = peaks[0]
        i = 1
        while i < len(peaks):
          count += peaks[i] - lowest[i-1]
          i += 1 
        return count
      
s = Solution()
print(s.minNumberOperations([3,1,5,4,2]))
     
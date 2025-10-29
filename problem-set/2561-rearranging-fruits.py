from typing import List
from collections import Counter


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq_basket1 = Counter(basket1)
        freq_basket2 = Counter(basket2)
        smallest = min(basket1 + basket2)
        diff_b1 = Counter()
        b1_keys = []
        for key in freq_basket1.keys():
          a, b = freq_basket1[key], freq_basket2[key]
          if (a + b) % 2 != 0:
            return -1
          diff = (a - b) // 2
          if diff > 0:
            diff_b1[key] = diff
            b1_keys.append(key)
          else:
            diff_b1[key] = 0
        
        diff_b2 = Counter()
        b2_keys = []
        for key in freq_basket2.keys():
          a, b = freq_basket1[key], freq_basket2[key]
          if (a + b) % 2 != 0:
            return -1
          diff = (b -a) // 2
          if diff > 0:
            diff_b2[key] = diff
            b2_keys.append(key)
          else:
            diff_b2[key] = 0
        
        b1_keys.sort()
        b2_keys.sort(reverse= True)
        b1, b2  = [] ,[]
        for key in b1_keys:
          b1.extend([key] * diff_b1[key])
        for key in b2_keys:
          b2.extend([key] * diff_b2[key])
        print(b1, b2)
        if len(b1) != len(b2):
          return -1
        
        cost = 0
        for i in range(len(b1)):
          cost += min(b1[i], b2[i], smallest * 2)
        
        return cost
      
      
s = Solution()
print("solution ", s.minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8]))
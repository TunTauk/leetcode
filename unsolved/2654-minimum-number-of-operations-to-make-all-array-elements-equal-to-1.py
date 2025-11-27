from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def gcd(num1: int, num2: int) -> int:
            while num1 > 0 and num2 > 0:
                if num1 > num2:
                    num1 %= num2
                else:
                    num2 %= num1
                    
            return num1 if num1 != 0 else num2
        
        i = 0
        l = len(nums)
        while i < l - 1:
            j = i
            while j < l - 1:
                if gcd(nums[j-i], nums[j + 1]) == 1:
                    return l + i 
                j += 1
            i += 1
        return -1
        
        

        
s =Solution()
print(s.minOperations(nums = [2,6,3,4]))
print(s.minOperations(nums = [2,10,6,14]))
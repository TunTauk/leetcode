class Solution(object):
    def removeDuplicates(self, nums):
      i = 0
      j = 1
      while i < len(nums)-1:
        if nums[i] != nums[i+1]:
          nums[j] = nums[i+1]
          j += 1
        i +=1
      return j
          
        
      
  
  
s = Solution()
print("solution ", s.removeDuplicates([0,0,1,2,2,3,4,5,5]))

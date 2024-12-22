class Solution(object):
    def searchInsert(self, nums, target):
      left = 0
      right = len(nums) - 1
      if target < nums[left]:
        return 0
      if target > nums[right]:
        return right + 1
      while left <= right:
        mid = int((left + right)/2)
        if target == nums[mid]:
          return mid
        if target > nums[mid]:
          left = mid + 1
        else:
          right = mid - 1
        print(left, mid, right)
      if target > nums[mid]:
        return mid + 1
      else:
        return mid
        
    
s = Solution()
print("solution ", s.searchInsert([1,3,5,6, 10, 12, 14], 11))